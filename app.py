from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in ", "info")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"you have been log out!, {user}", "info")
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        flash("Login Succesful", "info")
        return render_template("user.html", user=user)
    else:
        flash("You are no logged in ", "info")
        return redirect(url_for("login"))

@app.route("/test")
def test():
    return render_template("new.html")


if __name__ == "__main__":
    app.run(debug=True)
