from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def process_pdf(path: str):
    loader = PyPDFLoader(path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(chunks, embeddings)


def retrieve_from_vectorstores(query, vectorstores):
    results = []

    for i, vs in enumerate(vectorstores):
        docs = vs.similarity_search(query, k=2)
        for d in docs:
            d.metadata["source"] = f"vectorstore_{i}"
        results.extend(docs)

    return "\n".join(d.page_content for d in results)
