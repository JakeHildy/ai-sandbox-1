from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv

llm = OpenAI()

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"]
)
test_prompt = PromptTemplate(
    template="Write a test for the following {language} code:\n{code}",
    input_variables=["language", "code"]
)

# === CHAINS ===
code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt,
    output_key="code"
)
test_chain = LLMChain(
    llm=llm,
    prompt=test_prompt,
    output_key="test"
)

chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=["language", "task"],
    output_variables=["test", "code"]
)

async def homepage(request):
    body = await request.json()
    print (body)
    result = chain({
        "language": body["language"],
        "task": body["task"]
    })
    return PlainTextResponse(result["code"])

async def user_info(request):
    data = {"name": "John Doe", "age": 30}
    return JSONResponse(data)


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/user', user_info),
])