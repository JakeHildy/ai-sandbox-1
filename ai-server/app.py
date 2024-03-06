from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv
import prompts

llm = OpenAI(
    openai_api_key="",
)

render_prompt = PromptTemplate(
    template="{system_message}. Here is the prompt: {prompt}",
    input_variables=["prompt" "system_message"]
)
# test_prompt = PromptTemplate(
#     template="Write a test for the following {language} code:\n{code}",
#     input_variables=["language", "code"]
# )

# === CHAINS ===
render_chain = LLMChain(
    llm=llm,
    prompt=render_prompt,
    output_key="render"
)
# test_chain = LLMChain(
#     llm=llm,
#     prompt=test_prompt,
#     output_key="test"
# )

# chain = SequentialChain(
#     chains=[code_chain, test_chain],
#     input_variables=["language", "task"],
#     output_variables=["test", "code"]
# )

async def homepage(request):
    body = await request.json()
    print (body)
    result = render_chain({
        "prompt": body["prompt"],
        "system_message": prompts.getSystemMessage()
    })
    return PlainTextResponse(result["render"])

async def user_info(request):
    data = {"name": "John Doe", "age": 30}
    return JSONResponse(data)


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/user', user_info),
])