import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
);
""")
connection.commit()

# Insert data
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("Alice", 25, "alice@example.com"))
connection.commit()

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update data
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (28, "Alice"))
connection.commit()

# Delete data
cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))
connection.commit()

# Close the connection
connection.close()
