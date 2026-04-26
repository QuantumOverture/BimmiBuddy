from dotenv import load_dotenv

load_dotenv(override=True)
import os
from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands_tools import calculator

model = AnthropicModel(
    client_args={
        "api_key": os.getenv("ANTHROPIC_KEY", "MISSING_ANTHROPIC_KEY"),
    },
    # **model_config
    max_tokens=4096,
    model_id="claude-haiku-4-5",
    params={
        "temperature": 0.7,
    },
)

agent = Agent(model=model, tools=[calculator])
response = agent("What is 2+2")
print(response)
