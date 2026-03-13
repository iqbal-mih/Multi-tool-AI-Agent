🧠 Multi-Tool AI Agent (CSV → SQLite → SQL Agents → Master Agent)

This project builds a Multi-Agent AI system that can answer questions from multiple structured datasets using natural language.

The system converts CSV datasets into SQLite databases, creates SQL Agents for each database, wraps them as tools, and then uses a Master AI Agent to intelligently choose which tool to use based on the user's query.

In addition, the agent can also perform web search using DuckDuckGo when the query is not related to the datasets.

🚀 Features

Query multiple databases using natural language

Automatic agent routing to the correct database

SQL agents powered by LangChain

Web search tool using DuckDuckGo

Supports structured + unstructured queries

Built with LangChain + OpenAI-compatible LLM

🏗️ Architecture
User Question
      │
      ▼
Master AI Agent (Router)
      │
      ├── Heart Disease Tool → SQL Agent → heart_disease DB
      │
      ├── Cancer Tool → SQL Agent → cancer DB
      │
      ├── Diabetes Tool → SQL Agent → diabetes DB
      │
      └── Web Search Tool → DuckDuckGo

The Master Agent decides which tool to use automatically.

📂 Project Structure
project-root/
│
├── data/
│   ├── CSV_xlsx/
│   │   ├── heart.csv
│   │   ├── The_Cancer_data_1500_V2.csv
│   │   └── diabetes.csv
│   │
│   └── SQL_DB/
│       ├── heart.db        (auto created)
│       ├── cancer.db       (auto created)
│       └── diabetes.db     (auto created)
│
├── Multi Tool AI Agent main code.ipynb
└── README.md

⚠️ Important

The .db files will be automatically created when the notebook runs.

⚙️ Requirements

Python 3.9+

Jupyter Notebook

OpenAI-compatible API

Python Libraries

Install the required packages:

pip install pandas pyprojroot sqlalchemy langchain langchain-community langchain-openai duckduckgo-search jupyter
🔑 API Configuration

Inside the notebook you will see:

model_name = "..."
token = "..."
endpoint = "..."

Replace them with your actual values.

Example:

model_name = "gpt-4o"
token = "YOUR_API_KEY"
endpoint = "https://api.openai.com/v1"
▶️ How to Run the Project

Follow these steps to run the repository locally.

1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate it.

Windows
venv\Scripts\activate
Mac / Linux
source venv/bin/activate
3️⃣ Install Dependencies
pip install pandas pyprojroot sqlalchemy langchain langchain-community langchain-openai duckduckgo-search jupyter
4️⃣ Verify Data Folder

Make sure the CSV files exist:

data/CSV_xlsx/
heart.csv
The_Cancer_data_1500_V2.csv
diabetes.csv
5️⃣ Run Jupyter Notebook
jupyter notebook

Open the file:

Multi Tool AI Agent main code.ipynb
6️⃣ Run All Cells

Run the notebook from top to bottom.

The notebook will:

1️⃣ Load CSV files
2️⃣ Create SQLite databases
3️⃣ Store data in SQL tables
4️⃣ Create SQL agents
5️⃣ Wrap agents as tools
6️⃣ Build the master routing agent

7️⃣ Ask Questions

Example query:

agent_executor.invoke({
    "messages": [
        ("user","Tell me how many patients are over 50 years old in diabetes database?")
    ]
})
🧪 Example Queries
How many heart disease patients are male?

What is the average glucose level in diabetes dataset?

How many cancer patients are above 60 years old?

Search latest research on diabetes treatment

The master agent will automatically choose the correct tool.

🧠 Design Pattern

This project demonstrates Hierarchical Multi-Agent Architecture.

Components:

Component	Role
SQL Agents	Query individual databases
Tools	Wrap SQL agents
Master Agent	Decide which tool to call
DuckDuckGo Tool	Handle general knowledge queries
⚠️ Common Errors
no such table

Make sure the notebook cells that run:

df.to_sql(...)

have been executed.

NameError: here not defined

Add:

from pyprojroot import here
API errors

Check:

model_name
token
endpoint
📌 Why This Project Is Useful

This project demonstrates:

Multi-database AI systems

Tool-based agent orchestration

Natural language → SQL querying

Combining structured data + web search

This architecture is commonly used in AI data assistants and enterprise analytics agents.

👤 Author

Iqbal

AI / ML Enthusiast
LangChain | Multi-Agent Systems | Data AI

⭐ If you like this project

Consider giving it a ⭐ on GitHub!
