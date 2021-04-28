from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")  # Here the main page is defined
def home():
    return render_template("Indexpage.html")

@app.route("/<name>")               # This allows the user to go to different pages instead of the homepage
def user(name):                     # essentially it takes .../x the x as input and loads file x (for example: 127.0.0.1:5000/Indexpage.html loads Indexpage.html)
    return render_template({name})

# @app.route("/admin")  # This can be used to redirect user (for example now it redirects url/admin to url.)
# def admin():          # not very relevant for us yet.
#     return redirect(url_for("home"))

@app.route("/", methods=['GET', 'POST'])    # Check for current page if there are HTML forms with the methods Get and Post
def testbutton():                           #Function you want to define in the HTML form
    if request.method == "POST":            #Check if form method was post
        pong = "PONG"
        return render_template("Indexpage.html", testvariable = pong)              #Type pong on site
    else:
        return "Did not work"

if __name__ == "__main__":
    app.run()
