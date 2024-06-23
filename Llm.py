from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.prompts import PromptTemplate

model_path = '/home/shamit/proj/models/Phi-3-mini-4k-instruct-q4.gguf'

llm = LlamaCpp(
    model_path=model_path,
    temperature=0,
    max_tokens=200,
    #callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

template = """
## You are a helpful chatbot. Answer following question concisely. 
Question: {question}
"""

prompt_template = PromptTemplate.from_template(template)