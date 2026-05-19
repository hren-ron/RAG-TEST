from file_history_store import get_history
from vector_stores import VectorStoreService
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

import config_data as config

def print_promt(full_input):
    """

    :param full_input:
    :return:
    """
    print("用户提问：", end="")
    print(full_input.to_string())
    return full_input


class RagService(object):

    def __init__(self):

        self.vector_store = VectorStoreService(
            embedding=DashScopeEmbeddings(model=config.embedding_model_name)
        )

        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", "以我提供的参考资料为主，简洁专业的回答用户问题，参考资料：{context}"),
            ("system", "提供用户提供的历史会话记录，如下："),
            MessagesPlaceholder("history"),
            ("user", "请回答用户提问：{input}")
        ])

        self.chat_model = ChatTongyi(model=config.chat_model_name)

        self.chain = self.__get_chain()

    def __get_chain(self):
        """

        :return:
        """
        retriever = self.vector_store.get_retriever()

        def format_document(documents):
            if not documents:
                return ""
            return "\n".join([f"{d.page_content}\n" for d in documents])

        def format_for_retriever(value: dict):
            return value["input"]

        def format_for_prompt(value: dict):
            new_value = {}
            new_value["input"] = value["input"]["input"]
            new_value["context"] = value["context"]
            new_value["history"] = value["input"]["history"]
            return new_value

        chain = (
            {
                "input": RunnablePassthrough(),
                "context": RunnableLambda(format_for_retriever) | retriever | format_document
            } | RunnableLambda(format_for_prompt) | self.prompt_template | print_promt | self.chat_model | StrOutputParser()
        )

        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history"
        )

        return conversation_chain

if __name__ == "__main__":

    session_config = {
        "configurable": {
            "session_id": "session_001"
        }
    }


    rag_service = RagService()
    res = rag_service.chain.invoke({
        "input": "身高180，推荐尺码"
    }, session_config)
    print(res)