
from langchain_community.embeddings import DashScopeEmbeddings

model = DashScopeEmbeddings(model="text-embedding-v1")

print(model.embed_query("What is langchain?"))
print(model.embed_documents(["What is langchain?", "What is langchain?"]))