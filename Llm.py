from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.prompts import PromptTemplate

model_path = '/home/shamit/proj/models/Phi-3-mini-4k-instruct-q4.gguf'
#model_path = '/home/shamit/proj/models/microsoft/Phi-3-mini-4k-instruct_Q2_K.gguf'

llm = LlamaCpp(
    model_path=model_path,
    temperature=0,
    seed=37,
    max_tokens=50,
    #callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

template = """
## You are a helpful chatbot. Answer following question concisely. Keep the answer as brief as possible. 
Limit answer to 20 or 30 words. 
##Question: {question}
Answer: 
"""

prompt_template = PromptTemplate.from_template(template)
