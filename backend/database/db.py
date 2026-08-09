import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent / "notifyai.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            summary TEXT,
            category TEXT,
            importance INTEGER,
            urgency INTEGER,
            requires_action BOOLEAN,
            deadline TEXT,
            suggested_action TEXT,
            priority TEXT,
            priority_label TEXT,
            priority_score REAL,
            notification_action TEXT,
            notification_reason TEXT,
            is_read BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    connection.close()


def save_message(
    message: str,
    summary: str,
    category: str,
    importance: int,
    urgency: int,
    requires_action: bool,
    deadline: str | None,
    suggested_action: str | None,
    priority: str,
    priority_label: str,
    priority_score: float,
    notification_action: str,
    notification_reason: str
):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO messages (
            message,
            summary,
            category,
            importance,
            urgency,
            requires_action,
            deadline,
            suggested_action,
            priority,
            priority_label,
            priority_score,
            notification_action,
            notification_reason
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        message,
        summary,
        category,
        importance,
        urgency,
        requires_action,
        deadline,
        suggested_action,
        priority,
        priority_label,
        priority_score,
        notification_action,
        notification_reason
    ))

    connection.commit()

    message_id = cursor.lastrowid

    connection.close()

    return message_id


def get_messages():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM messages
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]


def get_unread_messages():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM messages
        WHERE is_read = 0
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]


def get_message_by_id(message_id: int):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM messages
        WHERE id = ?
    """, (message_id,))

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return dict(row)


def mark_message_as_read(message_id: int):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE messages
        SET is_read = 1
        WHERE id = ?
    """, (message_id,))

    connection.commit()

    connection.close()
