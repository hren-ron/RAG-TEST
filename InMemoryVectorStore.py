
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma


# vector_store = InMemoryVectorStore(
#     embedding=DashScopeEmbeddings()
# )

vector_store = Chroma(
    collection_name="test",
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./datas/chroma_db"
)

loader = CSVLoader(
    file_path="./datas/info.csv",
    encoding="utf-8",
    source_column="source"
)

docs = loader.load()


vector_store.add_documents(
    documents=docs,
    ids = ["id" + str(i) for i in range(1, len(docs) + 1)]
)

# vector_store.delete(ids=["id1", "id2"])

results = vector_store.similarity_search(
    query="python是不是世界上最好的语言",
    k=4
)

print(results)

