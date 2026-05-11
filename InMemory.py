
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory



model = ChatTongyi(model="qwen3-max")

prompt = PromptTemplate.from_template("会话历史：{chat_history}, 用户提问：{input}, 请回答")

str_parser = StrOutputParser()

def print_prompt(full_input):
    print(full_input)
    return full_input

base_chain = prompt | print_prompt | model | str_parser

store = {}

def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


conversation_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

if __name__ == "__main__":
    session_config = {
        "configurable": {
            "session_id": "session_001"
        }
    }

    res = conversation_chain.invoke({"input": "小明有两只狗"}, session_config)
    print(res)

    res = conversation_chain.invoke({"input": "小明又买了一只狗"}, session_config)
    print(res)

    res = conversation_chain.invoke({"input": "总共有几只狗"}, session_config)
    print(res)