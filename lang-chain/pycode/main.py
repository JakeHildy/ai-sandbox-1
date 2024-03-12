from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv

import argparse

load_dotenv()

# PromptTemplate, LLMChain, SequentialChain, OpenAI

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="Return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

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

result = chain({
    "language": args.language,
    "task": args.task
})

print('>>>>>>>>> CODE')
print(result["code"])
print('>>>>>>>>> TEST')
print(result["test"])

# def return_list():return [1, 2, 3, 4, 5]


# Lauch like this:
# python main.py --task "Return a function that describes all the solar systems largest moons" --language "python"


