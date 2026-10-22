from crewai import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()

# Create the Travel Planner Agent
travel_planner = Agent(
    role="Expert Travel Guide",
    goal="Provide curated, high-quality, and engaging travel recommendations for any destination.",
    backstory=(
        "You are a seasoned globetrotter and professional tour guide with years of experience "
        "exploring cities worldwide. You pride yourself on cutting through tourist traps to find "
        "the absolute best balance of iconic landmarks and authentic local experiences."
    ),
    verbose=True
)

 # Ask the user for a city
city = input("Enter a city you want to visit: ").strip()

# Create the Task
planning_task = Task(
    description=(
        f"Research the city of {city} and recommend exactly 3 must-visit places. "
        f"For each recommendation, provide the name of the place and a brief description "
        f"explaining why it is special."
    ),
    expected_output=(
        "A clean list containing exactly 3 places to visit in the specified city, "
        "with each entry featuring the name of the location and a concise 2-3 sentence description."
    ),
    agent=travel_planner
)

# Assemble the Crew
travel_crew = Crew(
    agents=[travel_planner],
    tasks=[planning_task],
    verbose=True
)



# Run the Crew and print the result
print(f"\n--- Generating recommendations for {city} ---\n")
result = travel_crew.kickoff()

print("\n--- Travel Recommendations ---")
print(result)
