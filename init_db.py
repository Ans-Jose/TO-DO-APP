import sqlite3

def init_db():
    conn = sqlite3.connect("data.db")  # creates data.db file if not exists
    c = conn.cursor()

    # table for your main to-do list
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            date TEXT,
            time TEXT
        )
    ''')

    # table for your past achievements
    c.execute('''
        CREATE TABLE IF NOT EXISTS past_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT NOT NULL   -- "success" or "failure"
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized ✅")
