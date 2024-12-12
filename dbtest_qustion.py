import streamlit as st
import sqlite3

# データベースへの接続（無ければ作成）
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# テーブルが無い場合は作成
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    hyouka TEXT
)
""")
conn.commit()

st.title("SQLite Write Example")

# 映画名入力
name_input = st.text_input("Enter a name to store in the database:")
# 感想入力
commnet_input = st.text_input("Enter a comment to store in the database:")

eiga1 = "ダイハード"
eiga2 = "ダイハード２"

options = st.multiselect(
    "What are your favorite colors",
    [f"{eiga1}", f"{eiga2}", "Red", "Blue"],
)

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    

st.write("You selected:", options)

if st.button("Add to Database"):
    if name_input:
        # DBに挿入
        cur.execute("INSERT INTO users (name,hyouka) VALUES (?)", (name_input,sentiment_mapping[selected],)) #ここの書き方変えてください
        conn.commit()
        st.success(f"'{name_input}' was added to the database!")
    else:
        st.warning("Please enter a name.")

st.write("## Current Database Entries")
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
st.write(rows)