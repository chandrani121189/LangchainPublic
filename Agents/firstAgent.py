from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM
llm = OpenAI(temperature=0)

# Load some basic tools (e.g., search, calculator)
tools = load_tools(["llm-math"], llm=llm)

# Initialize the agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Run the agent with a sample query
response = agent.run("What is the square root of 784, divided by 2?")
print(response)
