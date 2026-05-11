
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

model = ChatTongyi(model="qwen-max")

parser = StrOutputParser()

prompt = PromptTemplate.from_template("请给我一个唐诗")

chain = prompt | model | parser | model

res = chain.invoke(input={})
print(res.content) 