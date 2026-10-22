from dotenv import load_dotenv
from crewai import LLM
from crewai import Agent, Task, Crew

load_dotenv()


llm =  LLM(model="gpt-4.1-mini")

print("LLM Loaded Successfully")


writer = Agent(
    role="Writer",
    goal="Write Short , Simple text",
    backstory="You write clearly for beginners",
    llm = llm
)

print("Agent Created : ",  writer.role)


task = Task(
    description="Write a short 2-line poem about the moon",
    expected_output="A simple 2 line poem",
    agent=writer
)


crew = Crew(
    Agent=[writer],
    tasks=[task]
)

#ipynb
#result = await crew.kickoff_async()

# .py
result =  crew.kickoff()

print(result)