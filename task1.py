# weak code
from flask import Flask, request, session, jsonify
import sqlite3, hashlib

app = Flask(__name__)
app.secret_key = "dev"
def get_db():
    return sqlite3.connect("app.db")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    pw_hash = hashlib.md5(password.encode()).hexdigest()
    db = get_db()
    row = db.execute(
        "SELECT id, role FROM users WHERE username = '%s' AND pw_hash = '%s'"
        % (username, pw_hash)
    ).fetchone()
    if row:
        session["uid"] = row[0]
        session["role"] = row[1]
        return jsonify({"ok": True})
    return jsonify({"ok": False}), 401





# 1. vulnerable for SQL injection. 
# 2. uses MD5 for password hashing, which is not secure.
# 3. guessable secret key

