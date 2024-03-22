from dotenv import load_dotenv
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

from tools.test import tool

load_dotenv()

llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template("{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

tools=[tool]

agent = create_openai_functions_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)

agent_executor.invoke({"input": "Try running the test tool"})


