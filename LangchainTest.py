from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

res = model.invoke(input="你是谁")
print(res)

from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3.5:4b")
res = model.invoke(input="你是谁")
print(res)