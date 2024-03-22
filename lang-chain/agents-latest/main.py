from dotenv import load_dotenv

from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage

from tools.sql import list_tables, run_query_tool, describe_tables_tool
from tools.report import write_report_tool
from handlers.chat_model_start_handler import ChatModelStartHandler

load_dotenv()

handler = ChatModelStartHandler()
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, callbacks=[handler])
tables = list_tables()

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content=(
        "You are an AI that has access to an SQLite database.\n"
        f"The database has tables of: {tables}\n"
        "Do not make any assumptions about what tables exist "
        "or what columns exist. Instead, use the 'describe_tables' function"
        )
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
tools=[run_query_tool, describe_tables_tool, write_report_tool]

agent = create_openai_functions_agent(chat, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    # verbose=True,
    memory=memory
)

agent_executor.invoke({"input": "How many orders are there? Ensure you write the result to an html report and save it to the disk for all future queries."})
agent_executor.invoke({"input": "Repeat the exact same process for users and products."})

# agent_executor.invoke({"input": "what is 1 + 1?"})
# agent_executor.invoke({"input": "How about if I add one more?"})


