# AI Crew for Code Review Simulator
## Introduction

#### Code Review Simulator

By [chknim](https://github.com/chknim)

- [Pre-requisites](#pre-requisites)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Using Local Models with Ollama](#using-local-models-with-ollama)
- [License](#license)

## Pre-requisites
- `pip install poetry`
- Required when running a local model such as Ollama - `pip install -U langchain-community`
= Required when running a local model such as ChatGPT - `pip install -U langchain-openai`

## Running the Script
This example uses Ollama3 when running locally.

- **Configure Environment**: Copy ``.env.example` and set up the environment variable
- **Install Dependencies**: Run `poetry install --no-root`.
- **Execute the Script**: Run `python main.py` and input your idea.

## Details & Explanation
- **Running the Script**: Execute `python main.py`` and input the purpose of the code to be created and reviewed when prompted. The script will leverage the CrewAI framework to generate the code and get it reviewed with a detailed report to be finally generated.
- **Sample input**: "Write a function in javascript where given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n))."
- **Key Components**:
  - `./main.py`: Main script file.
  - `./tasks.py`: Main file with the tasks prompts.
  - `./agents.py`: Main file with the agents creation.

## Using Local Models with Ollama
The CrewAI framework supports integration with local models, such as Ollama, for enhanced flexibility and customization. This allows you to utilize your own models, which can be particularly useful for specialized tasks or data privacy concerns.

### Setting Up Ollama
- **Install Ollama**: Ensure that Ollama is properly installed in your environment. Follow the installation guide provided by Ollama for detailed instructions.
- **Configure Ollama**: Set up Ollama to work with your local model. You will probably need to [tweak the model using a Modelfile](https://github.com/jmorganca/ollama/blob/main/docs/modelfile.md), I'd recommend adding `Observation` as a stop word and playing with `top_p` and `temperature`.

### Integrating Ollama with CrewAI
- Instantiate Ollama Model: Create an instance of the Ollama model. You can specify the model and the base URL during instantiation. For example:

```python
from langchain.llms import Ollama
ollama_llama3 = Ollama(model="llama3")
# Pass Ollama Model to Agents: When creating your agents within the CrewAI framework, you can pass the Ollama model as an argument to the Agent constructor. For instance:

def local_expert(self):
	return Agent(
      role='My role',
      goal="""My goal""",
      backstory="""My backstory""",
      verbose=True,
      llm=ollama_llama3, # Ollama model passed here
    )
```

### Starting Up Ollama
- **Start the server**: For non-windows, start Ollama server from Start Menu or run `ollama serve`.  For Windows, start Ollama from Start Menu.


### Advantages of Using Local Models
- **Privacy**: Local models allow processing of data within your own infrastructure, ensuring data privacy.
- **Customization**: You can customize the model to better suit the specific needs of your tasks.
- **Performance**: Depending on your setup, local models can offer performance benefits, especially in terms of latency.

### Disadvantages of Using Local Model
- **Performance**: Depending on your device, local models may take excessively long to generate a result and may be worse with multiple iterations in Agentic Workflow.

## License
This project is released under the MIT License.