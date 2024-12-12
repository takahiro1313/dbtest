import streamlit as st
import sqlite3

# データベースへの接続（無ければ作成）
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# テーブルが無い場合は作成
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")
conn.commit()

st.title("SQLite Write Example")

# ユーザー入力
name_input = st.text_input("Enter a name to store in the database:")

if st.button("Add to Database"):
    if name_input:
        # DBに挿入
        cur.execute("INSERT INTO users (name) VALUES (?)", (name_input,))
        conn.commit()
        st.success(f"'{name_input}' was added to the database!")
    else:
        st.warning("Please enter a name.")

st.write("## Current Database Entries")
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
st.write(rows)
