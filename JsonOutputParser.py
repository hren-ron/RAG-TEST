

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatTongyi(model="qwen-max")

first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}, 刚生了：{gender}, 请帮我起名字。"
    "封装为json格式，key为name, value为名字"
)

second_prompt = PromptTemplate.from_template(
    "姓名：{name}, 帮我解析其含义"
)

chain = first_prompt | model | json_parser | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "王", "gender": "男"}):
    print(chunk, end="", flush=True) 