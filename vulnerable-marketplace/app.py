from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)
DB_NAME = "users.db"

def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("CREATE TABLE users(username TEXT, password TEXT)")
        c.execute("INSERT INTO users VALUES('admin','admin')")
        conn.commit()
        conn.close()
        print("Database initialized")

def get_db():
    return sqlite3.connect(DB_NAME)

@app.route("/")
def home():
    return """
    <h1>Demo Marketplace</h1>
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit">
    </form>
    """

# Intentional SQL Injection vulnerability
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = get_db()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return "Login successful"
    else:
        return "Login failed"

if __name__ == "__main__":
    init_db()
    app.run(port=5000)
