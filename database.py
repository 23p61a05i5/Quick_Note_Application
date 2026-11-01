import sqlite3
from pathlib import Path
DB=Path(__file__).with_name("app.db")
def connect():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def init_db():
    with connect() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL, body TEXT NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
if __name__=="__main__": init_db(); print("Notes database initialized.")
