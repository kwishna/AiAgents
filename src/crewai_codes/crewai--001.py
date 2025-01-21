"""
pip install crewai
pip install 'crewai[tools]'
pip install ollama

Objectives:
    1. Build a multi-agent system for image classification, description, and information retrieval using CrewAI.
    2. Automate decision-making: Agents perform specific tasks like identifying animals in images, describing them, and fetching relevant facts.
    3. Task sequencing: Coordinate agents through tasks in a stepwise, agentic system.
"""

from crewai import Agent, Task, Crew

"""
Define the Agents:
    Classifier Agent: Checks if the image contains an animal, uses llava:7b model to classify the animal.
    Description Agent: Describes the animal in the image. This also uses the same llava:7b model like the preceding agent.
    Information Retrieval Agent: This agent retrieves additional information or interesting facts about the animal. It uses llama2 to provide this information.
"""

# 1. Image Classifier Agent (to check if the image is an animal)
classifier_agent = Agent(
    role="Image Classifier Agent",
    goal="Determine if the image is of an animal or not",
    backstory="""
    You have an eye for animals! Your job is to identify whether the input image is of an animal or something else.
    """,
    llm='ollama/llava:7b' # Model for image-related tasks

)

# 2. Animal Description Agent (to describe the animal in the image)
description_agent = Agent(
    role="Animal Description Agent {image_path}",
    goal="Describe the animal in the image",
    backstory="""
    You love nature and animals. Your task is to describe any animal based on an image.
    """,
    llm='ollama/llava:7b' # Model for image-related tasks
)

# 3. Information Retrieval Agent (to fetch additional info about the animal)
info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain animal",
    backstory="""
    You are very good at telling interesting facts. You don't give any wrong information if you don't know it.
    """,
    llm='ollama/llama2' # Model for general knowledge retrieval
)

"""
Define Tasks for Each Agent:
    Task 1: Classify whether the image contains an animal.
    Task 2: If the image is classified as an animal, describe it.
    Task 3: Provide additional information about the animal based on the description.
"""
# Task 1: Check if the image is an animal
task1 = Task(
    description="Classify the image ({image_path}) and tell me if it's an animal.",
    expected_output="If it's an animal, say 'animal'; otherwise, say 'not an animal'.",
    agent=classifier_agent

)

# Task 2: If it's an animal, describe it
task2 = Task(
    description="Describe the animal in the image.({image_path})",
    expected_output="Give a detailed description of the animal.",
    agent=description_agent
)

# Task 3: Provide more information about the animal
task3 = Task(
    description="Give additional information about the described animal.",
    expected_output="Provide at least 5 interesting facts or information about the animal.",
    agent=info_agent
)

# Crew to manage the agents and tasks
crew = Crew(
    agents=[classifier_agent, description_agent, info_agent],
    tasks=[task1, task2, task3],
    verbose=True
)

# Execute the tasks with the provided image path
result = crew.kickoff(inputs={'image_path': 'racoon.jpg'})