import os
from dotenv import load_dotenv

from griptape.structures import Agent
from griptape.drivers import OpenAiChatPromptDriver
from griptape.rules import Rule
from griptape.config import StructureConfig, StructureGlobalDriversConfig

load_dotenv() # Load the environment variables

# Create The Agent
agent = Agent(
    config=StructureConfig(
        global_drivers=StructureGlobalDriversConfig(
            prompt_driver=OpenAiChatPromptDriver(
                api_key=os.environ["OPENAI_API_KEY"],
                temperature=0.1,
                model="gpt-3.5-turbo",
                response_format="json_object",
                seed=42,
            )
        )
    ),
    input_template="You will be provided with a description of a mood, and your task is to generate the CSS code for a color that matches it. Description: {{ args[0] }}",
    rules=[
        Rule(
            value='Write your output in json with a single key called "css_code".'
        )
    ],
)

# Run The Agent
agent.run("Give me a haiku about skateboarding")
