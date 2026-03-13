🧠 Multi-Tool AI Agent
CSV → SQLite → SQL Agents → Master Routing Agent








A Multi-Agent AI system that can answer questions from multiple structured datasets using natural language.

This project converts CSV datasets into SQLite databases, creates SQL Agents for each dataset, wraps them as tools, and then uses a Master AI Agent to decide which database to query.

The system can also perform web search using DuckDuckGo for questions unrelated to the datasets.

🚀 Features

✅ Natural language queries over multiple databases
✅ Automatic tool routing by a master agent
✅ SQL Agents powered by LangChain
✅ Web search integration (DuckDuckGo)
✅ Supports structured + unstructured queries
✅ Scalable multi-agent architecture

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

The Master Agent automatically selects the correct tool based on the user’s question.

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
│       ├── heart.db
│       ├── cancer.db
│       └── diabetes.db
│
├── Multi Tool AI Agent main code.ipynb
└── README.md

⚠️ Note:
The .db files are automatically created when the notebook runs.

⚙️ Requirements

Python 3.9+

Jupyter Notebook

OpenAI-compatible API

Install Dependencies
pip install pandas pyprojroot sqlalchemy langchain langchain-community langchain-openai duckduckgo-search jupyter
⚡ Quick Start
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create virtual environment
python -m venv venv

Activate it.

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install pandas pyprojroot sqlalchemy langchain langchain-community langchain-openai duckduckgo-search jupyter
4️⃣ Run Jupyter Notebook
jupyter notebook

Open:

Multi Tool AI Agent main code.ipynb

Run the notebook from top to bottom.

🧪 Example Queries
How many heart disease patients are male?

What is the average glucose level in diabetes dataset?

How many cancer patients are above 60 years old?

Search latest research on diabetes treatment

The Master Agent will automatically choose the correct tool.

🧠 How It Works

1️⃣ Load CSV datasets
2️⃣ Convert datasets to SQLite databases
3️⃣ Create SQL Agents for each database
4️⃣ Wrap SQL agents as LangChain tools
5️⃣ Build a Master Agent that routes queries
6️⃣ Execute natural language questions

⚠️ Common Errors
no such table

Make sure the notebook cells that run:

df.to_sql(...)

have been executed.

NameError: here not defined

Add:

from pyprojroot import here
API Key Error

Make sure these variables are set in the notebook:

model_name
token
endpoint
📌 Why This Project Matters

This project demonstrates:

Multi-agent AI systems

Natural language → SQL querying

Tool-based agent orchestration

Combining structured data + web search

This architecture is used in AI data assistants and enterprise analytics systems.

👤 Author

Iqbal

AI / ML Enthusiast
LangChain | Multi-Agent Systems | Data AI

⭐ Support

If you find this project useful, please consider starring the repository ⭐.
