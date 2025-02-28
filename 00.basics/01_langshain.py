### langshain -> langchain
from langchain_community.llms import Ollama
llm = Ollama(model="gemma2:2b") 


for chunks in llm.stream("FIFA oragization in MAX 5 lines"):
    print(chunks, end='\n')
