from dotenv import load_dotenv

from griptape.structures import Agent

load_dotenv() # Load the environment variables

# Create The Agent
agent = Agent()

# Run The Agent
agent.run("Give me a haiku about skateboarding")