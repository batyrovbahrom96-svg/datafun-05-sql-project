import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Load schema.sql
with open("sql/schema.sql") as f:
    cursor.executescript(f.read())

# Load insert.sql
with open("sql/insert.sql") as f:
    cursor.executescript(f.read())

conn.commit()

# Show authors
df_authors = pd.read_sql_query("SELECT * FROM authors", conn)
print("\nAuthors in DB:")
print(df_authors)

# Show books before update
df_books = pd.read_sql_query("SELECT * FROM books", conn)
print("\nBooks before update:")
print(df_books)

# Update a book
cursor.execute("UPDATE books SET title='Emma' WHERE book_id=3")
conn.commit()

# Show books after update
df_books_after = pd.read_sql_query("SELECT * FROM books", conn)
print("\nBooks after update:")
print(df_books_after)

# ✅ Close AFTER everything
conn.close()