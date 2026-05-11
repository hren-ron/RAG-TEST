from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
chat_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个边塞诗人，可以作诗"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "请来作一首唐诗")
])

history_data = [
    ("human", "请来作一首唐诗"),
    ("assistant", "窗前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human", "请给我一个唐诗"),
    ("assistant", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦")
]

prompt_text = chat_template.invoke(input={"chat_history": history_data}).to_string()

print(prompt_text)

model = ChatTongyi(model="qwen-max")
response = model.invoke(prompt_text)
print(response.content)