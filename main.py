from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from tasks import CodeReviewTasks
from agents import CodeReviewAgents

tasks = CodeReviewTasks()
agents = CodeReviewAgents()

print("## Welcome to the Code Review Crew")
print('-------------------------------')
code = input("What is the code you would like to build? What will be the goals?\n")

# Create Agents
coder = agents.software_engineer()
reviewer = agents.staff_software_engineer()


# Create Tasks
write_code = tasks.code_task(coder, code)
review_code = tasks.review_task(reviewer, code)

# Create Crew responsible for the code
crew = Crew(
  agents=[
    coder,
    reviewer
  ],
  tasks=[
    write_code,
    review_code
  ],
  verbose=True
)

code_output = crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code as you requested:")
print(code_output)
