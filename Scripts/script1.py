from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")  # Here the main page is defined
def home():
    return "Hello! this is the main page <h1>HELLO<h1>"

@app.route("/<name>")  # This can be used to show dynamic names on pages, for example now url/home shows "home" as name.
def user(name):        # Not very relevant for us.
    return f"Hello {name}!"

@app.route("/admin")  # This can be used to redirect user (for example now it redirects url/admin to url.)
def admin():          # not very relevant for us yet.
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()