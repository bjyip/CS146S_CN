import sqlite3
from contextlib import closing
from pathlib import Path


def save_note(path: Path, content: str) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(path)) as db, db:
        db.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT NOT NULL)")
        return db.execute("INSERT INTO notes (content) VALUES (?)", (content,)).lastrowid


def list_notes(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    with closing(sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)) as db:
        return [
            {"id": note_id, "content": content}
            for note_id, content in db.execute("SELECT id, content FROM notes ORDER BY id DESC")
        ]
