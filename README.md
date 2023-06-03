# Getting-started-with-langchain
A Langchain LLM experimental repository. 

This repository contains code to experiment with langchain a LLM.

To run the code -
Enter your openai API key in the apikey.py file
You can install the dependancies from the requirements.txt or run the code in 'langchain' venv

About the code -
This code currently experiments with Prompt Templates, LLMChain, Simple Sequential Chain, Sequential Chain, Conversation Buffer Memory, and Wikipedia API.
It works as a autogpt and outputs to the prompt. The prompt here is a template for blog topic. The langchain llm created generates title and script for the blog topic while leveraging wikipedia research using the Wikipedia API Wrapper. It also displays the history of prompts and outputs using the conversation buffer memory.

This is a experimental repository and anyone who wants to contribute and experiment is welcome!

You are free to make advancements on your own, while here are some points to be worked on :
- The conversation buffer memory outputs in the format of Human:{prompt text} AI:{Response text}. How could we format this ?
- Experimenting wwith the memory 
- Efficiency at chaining (Here, simple sequential and sequential chains are used)

