from fastapi import FastAPI, Query
from pydantic import BaseModel
import pandas as pd
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import os

app = FastAPI(title="Multi-Tool AI Agent for Medical Datasets")

# Load datasets
heart_df = pd.read_csv('data/CSV_xlsx/heart.csv')
cancer_df = pd.read_csv('data/CSV_xlsx/The_Cancer_data_1500_V2.csv')
diabetes_df = pd.read_csv('data/CSV_xlsx/diabetes.csv')

# Setup SQL engines
engine1 = create_engine('sqlite:///data/heart_disease.db')
engine2 = create_engine('sqlite:///data/cancer.db')
engine3 = create_engine('sqlite:///data/diabetes.db')

heart_df.to_sql("heart_disease", engine1, index=False, if_exists="replace")
cancer_df.to_sql("cancer", engine2, index=False, if_exists="replace")
diabetes_df.to_sql("diabetes", engine3, index=False, if_exists="replace")

db1 = SQLDatabase(engine=engine1)
db2 = SQLDatabase(engine=engine2)
db3 = SQLDatabase(engine=engine3)

# Setup LLM
os.environ['GITHUB_TOKEN'] = "..."  # Replace with your actual GitHub token
token = os.environ.get("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4.1-mini"
llm = ChatOpenAI(
    model_name=model_name,
    openai_api_key=token,
    openai_api_base=endpoint,
    temperature=0.5,
)

agent_tool1 = create_sql_agent(llm, db=db1, agent_type="openai-tools", verbose=True)
agent_tool2 = create_sql_agent(llm, db=db2, agent_type="openai-tools", verbose=True)
agent_tool3 = create_sql_agent(llm, db=db3, agent_type="openai-tools", verbose=True)


# Define tools for agent
@tool
def heart_disease_db(question: str) -> str:
    """
    Use this tool to answer questions related to the heart disease database.
    """
    result = agent_tool1.invoke({"input": question})
    return result["output"]

@tool
def cancer_db(question: str) -> str:
    """
    Use this tool to answer questions related to the cancer database.
    """
    result = agent_tool2.invoke({"input": question})
    return result["output"]

@tool
def diabetes_db(question: str) -> str:
    """
    Use this tool to answer questions related to the diabetes database.
    """
    result = agent_tool3.invoke({"input": question})
    return result["output"]

search_tool = DuckDuckGoSearchRun()

try:
    from langchain.agents import create_react_agent
except ImportError:
    from langgraph.prebuilt import create_react_agent

agent_executor = create_react_agent(
    model=llm,
    tools=[heart_disease_db, cancer_db, diabetes_db, search_tool],
)

class AgentRequest(BaseModel):
    question: str

@app.post("/agent")
def agent_query(request: AgentRequest):
    result = agent_executor.invoke({"messages": [("user", request.question)]})
    final_message = result["messages"][-1]
    return {"answer": final_message.content}
