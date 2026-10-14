# weak code
import time, hashlib
from flask import Flask, request
app = Flask(__name__)
tokens = {}
@app.route("/forgot", methods=["POST"])
def forgot():
    email = request.form ["email"]
    user = find_user (email)
    if not user:
        return "No account with that email", 404
    token = hashlib.md5(str(int(time.time())).encode()).hexdigest()
    tokens [token] = user.id
    link = "https://" + request.headers["Host"] + "/reset?token=" + token
    send_mail(email, "Reset your password: "  + link)
    return "Reset email sent"
@app.route("/reset", methods=["POST"])
def reset():
    token = request.form ["token"]
    uid = tokens.get (token)
    if uid is None:
        return "Invalid", 400
    set_password(uid, request.form ["password"])
    return "Password updated"



"""
1. Predictable reset token
2. No token expiry
3. User enumeration
"""
