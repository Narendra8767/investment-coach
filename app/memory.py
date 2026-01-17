from datetime import datetime
from app.database import get_connection

def create_chat(session_id: str, title: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO chats (session_id, title, created_at)
    VALUES (?, ?, ?)
    """, (session_id, title, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def add_message(session_id: str, role: str, content: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO messages (session_id, role, content, created_at)
    VALUES (?, ?, ?, ?)
    """, (session_id, role, content, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def get_chat(session_id: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT role, content FROM messages
    WHERE session_id = ?
    ORDER BY id ASC
    """, (session_id,))

    rows = cur.fetchall()
    conn.close()

    return [{"role": r, "content": c} for r, c in rows]


def list_chats():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT session_id, title, created_at
    FROM chats
    ORDER BY created_at DESC
    """)

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "session_id": sid,
            "title": title,
            "created_at": created
        }
        for sid, title, created in rows
    ]
