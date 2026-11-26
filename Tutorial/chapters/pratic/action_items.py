"""An offline, fixture-based starting point for the action-item project."""

import argparse
import json
import sqlite3
from contextlib import closing
from pathlib import Path

NOTE = "明天检查日志；发布已完成。"
MODEL_CANDIDATES = ("明天检查日志",)


def preview(simulate_failure=False):
    # This toy rule applies to the fixture only, not arbitrary meeting notes.
    candidates = (
        [sentence for sentence in NOTE.split("；") if sentence.startswith("明天")]
        if simulate_failure
        else list(MODEL_CANDIDATES)
    )
    return {
        "note": NOTE,
        "candidates": candidates,
        "source": "fixture_rule" if simulate_failure else "fixture_model",
        "error": "simulated_timeout" if simulate_failure else None,
    }


def save(db, text, *, confirmed=False):
    if not confirmed or not text.strip():
        raise ValueError("save requires confirmation and non-empty text")
    with closing(sqlite3.connect(db)) as connection, connection:
        connection.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, text TEXT)")
        cursor = connection.execute("INSERT INTO tasks (text) VALUES (?)", (text.strip(),))
        return cursor.lastrowid


def list_items(db):
    # Opening in read-only mode does not create an empty database on a bad path.
    uri = Path(db).resolve().as_uri() + "?mode=ro"
    with closing(sqlite3.connect(uri, uri=True)) as connection:
        return [
            {"id": item_id, "text": text}
            for item_id, text in connection.execute("SELECT id, text FROM tasks ORDER BY id")
        ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("preview").add_argument("--simulate-failure", action="store_true")
    save_command = commands.add_parser("save")
    save_command.add_argument("--confirm", action="store_true", required=True)
    save_command.add_argument("text")
    commands.add_parser("list")
    args = parser.parse_args()

    try:
        if args.command == "preview":
            result = preview(args.simulate_failure)
        elif args.db is None:
            parser.error("save and list require --db")
        elif args.command == "save":
            result = {"id": save(args.db, args.text, confirmed=args.confirm)}
        else:
            result = list_items(args.db)
    except (sqlite3.Error, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False))
