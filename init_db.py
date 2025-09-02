import sqlite3

def init_db():
    conn = sqlite3.connect("data.db")  # creates data.db if not exists
    c = conn.cursor()

    # table for main to-do list with user_id
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            date TEXT,
            time TEXT,
            user_id TEXT NOT NULL
        )
    ''')

    # table for past achievements with user_id
    c.execute('''
        CREATE TABLE IF NOT EXISTS past_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT NOT NULL,   -- "success" or "failure"
            user_id TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized ✅")
