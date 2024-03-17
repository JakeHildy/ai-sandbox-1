from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = ChatOpenAI()
output_parser = StrOutputParser()

input = "i need json that defines a React component that has a button that says 'click me'"

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are expert in creating json structures that defines a React component"),
    ("user", "{input}")
])

chain = prompt | llm | output_parser

response = chain.invoke({"input": input})

print('\n========================')
print(response)




