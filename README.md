# Task 1 — Quick Note

A single-page notes app: POST requests save notes to SQLite and the same page renders the saved notes.

## Project structure
- `app.py` — Flask routes and request handling
- `database.py` — SQLite database initialization
- `templates/index.html` — Jinja frontend
- `static/css/main.css` — page styling
- `static/js/main.js` — client-side interactions
- `app.db` — generated SQLite database

## Run locally
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python database.py
python app.py
```
Then open http://127.0.0.1:5000

This is a learning project inspired by the Flask + SQLite tutorial project structure. Before public deployment, disable debug mode and add production security configuration.
