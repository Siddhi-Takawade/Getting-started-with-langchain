import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = apikey

#frontend
st.title('Langchain AutoGPT')
prompt = st.text_input('Give your prompt here!')

title_template = PromptTemplate(
    input_variables = ['topic'],
    template='Write me a blog title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'],
    template='Write me a blog script based on this title TITLE: {title} while leveraging on this wikipedia research: {wikipedia_research}'
)

#memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

#memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')

#llm
llm = OpenAI(temperature=0.9) #tells how creative model will be
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)
#simple_sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=['topic'], output_variables=['title', 'script'], verbose=True)

wiki = WikipediaAPIWrapper()
#show prompt
if prompt:
    #response = simple_sequential_chain.run(prompt)
    #response = sequential_chain({'topic':prompt})
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)
    st.write(title)
    st.write(script)
    #st.write(response['title'])
    #st.write(response['script'])

    with st.expander('Title History'):
        st.info(title_memory.buffer)

    with st.expander('Script History'):
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'):
        st.info(wiki_research)