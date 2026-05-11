
import os, json
from typing import Sequence

from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

class FileChatMessageHistory(BaseChatMessageHistory):
    """Chat message history stored in a file."""

    def __init__(self, session_id: str, storage_path: str):
        self.session_id = session_id
        self.storage_path = storage_path

        self.file_path = os.path.join(self.storage_path, self.session_id)

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)

        new_messages = [message_to_dict(m) for m in all_messages]

        with open(self.file_path, "w") as f:
            json.dump(new_messages, f)

    @property
    def messages(self):

        try:
            with open(self.file_path, "r") as f:
                message_data = json.load(f)

            return messages_from_dict(message_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump([], f)



model = ChatTongyi(model="qwen3-max")

prompt = PromptTemplate.from_template("会话历史：{chat_history}, 用户提问：{input}, 请回答")

str_parser = StrOutputParser()

def print_prompt(full_input):
    print(full_input)
    return full_input

base_chain = prompt | print_prompt | model | str_parser

store = {}

def get_history(session_id):

    return FileChatMessageHistory(session_id, "./storage")

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

    # res = conversation_chain.invoke({"input": "小明有两只狗"}, session_config)
    # print(res)
    #
    # res = conversation_chain.invoke({"input": "小明又买了一只狗"}, session_config)
    # print(res)

    res = conversation_chain.invoke({"input": "总共有几只狗"}, session_config)
    print(res)