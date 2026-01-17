from collections import defaultdict

SESSION_VECTORSTORES = defaultdict(list)

def add_vectorstore(session_id, vectorstore):
    SESSION_VECTORSTORES[session_id].append(vectorstore)

def get_vectorstores(session_id):
    return SESSION_VECTORSTORES.get(session_id, [])
