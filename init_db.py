import sqlite3

def init_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    # ---- Create tables if not exist ----
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            date TEXT,
            time TEXT,
            user_id TEXT NOT NULL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS past_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT NOT NULL,
            user_id TEXT NOT NULL
        )
    ''')

    # ---- Add user_id column to old tables if missing ----
    try:
        c.execute("ALTER TABLE tasks ADD COLUMN user_id TEXT;")
    except sqlite3.OperationalError:
        pass  # column already exists

    try:
        c.execute("ALTER TABLE past_tasks ADD COLUMN user_id TEXT;")
    except sqlite3.OperationalError:
        pass  # column already exists

    # ---- Update old rows to have default user_id ----
    c.execute("UPDATE tasks SET user_id = 'default_user' WHERE user_id IS NULL;")
    c.execute("UPDATE past_tasks SET user_id = 'default_user' WHERE user_id IS NULL;")

    conn.commit()
    conn.close()
    print("Database initialized and old rows updated ✅")


if __name__ == "__main__":
    init_db()
