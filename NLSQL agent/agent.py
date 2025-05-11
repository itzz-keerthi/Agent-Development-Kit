from dotenv import load_dotenv
from google.adk.agents import Agent
from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine 
from llama_index.llms.gemini import Gemini
import os 
from llama_index.core import Settings
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
llm = Gemini(api_key=gemini_api_key, model="models/gemini-1.5-flash")
db_path = r"D:\Learnings\generativeAI\Learning_ADK\employees.db"
sqlite_uri = f"sqlite:///{db_path}"
table_name = "employees"
# llm = Gemini(model_name="models/gemini-1.5-flash")
sql_database = SQLDatabase.from_uri(sqlite_uri)
embed_model = GeminiEmbedding(model_name="models/embedding-001")
Settings.llm = llm
Settings.embed_model = embed_model

sql_query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=[table_name],
    llm=llm
)

# print(response)

def nlsql_tool(query:str) -> dict: 
    response=sql_query_engine.query(query)
    if response:
        return {
            "status": "success",
            "report": response.response,
        }
    else:
        return {
            "status": "success",
            "report": "Insufficient information to answer the question.",
        }

result=nlsql_tool("tell me about John Doe")
print(result.get('report'))

root_agent = Agent(
    name="employee_info_agent",
    model="gemini-1.5-flash",
    description="Answers questions about employee information using the provided tools only.",
    instruction="If a user asks a query, use the tool to get details from the database. NOTE: Use only the provided tool, if you don't have the answer provide Insufficent data",
    tools=[nlsql_tool],
)