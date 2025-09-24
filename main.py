import sqlite3
import pandas as pd

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Run schema
with open("sql/schema.sql") as f:
    cursor.executescript(f.read())

# Run inserts
with open("sql/insert.sql") as f:
    cursor.executescript(f.read())

# Query before update
print("Books before update:")
df1 = pd.read_sql_query("SELECT * FROM books", conn)
print(df1)

# Run update query
cursor.execute("UPDATE books SET title='Emma' WHERE book_id='3'")
conn.commit()

# Query after update
print("\nBooks after update:")
df2 = pd.read_sql_query("SELECT * FROM books", conn)
print(df2)

conn.close()