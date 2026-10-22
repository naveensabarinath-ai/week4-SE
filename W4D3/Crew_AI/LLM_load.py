from dotenv import load_dotenv
from crewai import LLM
from crewai import Agent

load_dotenv()


llm =  LLM(model="geo-41-mini")

print("LLM Loaded Successfully")


guide = Agent(
    role="Travel Guid",
    goal="Suggest fun places to visit",
    backstory="You Toured about 50 countries",
    llm = llm,
    verbose = True
)

print("Agent Created : ",  guide.role)