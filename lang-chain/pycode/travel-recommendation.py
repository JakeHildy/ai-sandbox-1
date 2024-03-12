from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI()

user_input = {
    "destination": "Kyoto, Japan",
    "date": "2023-04-15",
    "interests": ["historical sites", "local cuisine"],
    "budget": "moderate",
    "weather": "sunny",
    "current_events": ["Cherry Blossom Festival"]
}


# Creating the prompt template
itinerary_prompt = PromptTemplate(
    template="""
    Given the destination {destination} on {date}, with expected {weather} weather and the ongoing {current_events},
    create a detailed itinerary for a traveler interested in {interests} with a {budget} budget. The plan should include
    morning, afternoon, and evening activities, along with suggested dining options.
    """,
    input_variables=["destination", "date", "interests", "budget", "weather", "current_events"]
)

test_chain = LLMChain(
    llm=llm,
    prompt=itinerary_prompt,
    # output_key="itinerary"
)

# Running the chain
result = test_chain.invoke(user_input)
print(result['text'])

