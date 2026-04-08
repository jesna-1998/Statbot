import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def create_agent(csv_path):
    df = pd.read_csv(csv_path)

    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo"
    )

    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        allow_dangerous_code=True
    )

    return agent, df