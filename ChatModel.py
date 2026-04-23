

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


model = ChatTongyi(model="qwen3-max")

messages = [
    # SystemMessage(content="你是一个边塞诗人"),
    ('system', "你是一个边塞诗人"),
    ('human', "你写一首唐诗")
    #HumanMessage(content="写一首唐诗")
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk.content, end=" ", flush=True)
