# LangChain Zero-Shot ReAct Agent Example

This project demonstrates how to create and run a **LangChain agent** using **OpenAI** with a **Zero-Shot ReAct** setup.  
The agent is capable of reasoning about a task and using tools (like `llm-math`) without prior examples.

---

## 📋 Features
- Uses **OpenAI LLM** for reasoning.
- Loads built-in LangChain tools (e.g., math).
- Implements a **zero-shot-react-description** agent.
- Executes queries and returns results with reasoning steps.

---

## 🛠️ Requirements
- Python 3.9+
- An [OpenAI API key](https://platform.openai.com/)
- The following Python packages:
  ```bash
  pip install langchain openai python-dotenv
  ```

---

## 📂 Setup
1. **Clone this repository** or copy the code into a `.py` file.
2. **Create a `.env` file** in the project root with:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
3. **Install dependencies**:
   ```bash
   pip install langchain openai python-dotenv
   ```

---

## 🚀 Usage
Run the script:

```bash
python agent_example.py
```

Example code:
```python
from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = OpenAI(temperature=0)

# Load tools (e.g., calculator)
tools = load_tools(["llm-math"], llm=llm)

# Initialize the agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Run a sample query
response = agent.run("What is the square root of 784, divided by 2?")
print(response)
```

---

## 📊 Example Output
```text
> Entering new AgentExecutor chain...
I will calculate the square root of 784, then divide by 2.
Square root of 784 = 28
28 ÷ 2 = 14
Final answer: 14
> Finished chain.
14
```

---

## 📚 References
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
