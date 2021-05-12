import os
import sys
from os.path import join, dirname, realpath

import flask
from flask import Flask, redirect, url_for, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import json
from extract_csv import extract_data
import numpy as np

upload_folder = join(dirname(realpath(__file__)), 'csv_files/')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['UPLOAD_EXTENSIONS'] = ['.csv']

uploadedFiles = []
csvFilesPos = []
csvFilesName = []


@app.route("/")  # Here the main page is defined
def home():
    return render_template("Indexpage.html")

@app.route("/<name>")               # This allows the user to go to different pages instead of the homepage
def user(name):                     # essentially it takes .../x the x as input and loads file x (for example: 127.0.0.1:5000/Indexpage.html loads Indexpage.html)
    return render_template({name}, Arraynames = csvFilesName)

# @app.route("/admin")  # This can be used to redirect user (for example now it redirects url/admin to url.)
# def admin():          # not very relevant for us yet.
#     return redirect(url_for("home"))

@app.route("/Indexpage", methods=['GET', 'POST'])    # Check for current page if there are HTML forms with the methods Get and Post
def testbutton():                           #Function you want to define in the HTML form
    if request.method == "POST":            #Check if form method was post
        pong = "PONG"
        return render_template("Indexpage.html", testvariable = pong)              #Type pong on site
    else:
        return "Did not work"

@app.route('/upload_file', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        uploadname = request.form['fileName']
        uploaded_file = request.files['file']                   #Get the file from the request
        filename = secure_filename(uploaded_file.filename)      #Check if someone didnt do something weird with the file

        if filename != '':                                      #Check if filename is not empty
            file_ext = os.path.splitext(filename)[1]                #Split the extensions
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:     #Check if it is a valid extension
                abort(400)

            csvFilesName.append(uploadname)
            csvFilesPos.append(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploadedFiles.append(uploaded_file)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) #upload file to correct position
            return render_template('Visualisation.html', Arraynames = csvFilesName)

    return render_template('Visualisation.html', Arraynames = csvFilesName)

@app.route('/getData', methods=['GET','POST'])
def getData():
    if request.method == 'POST':
        fileSelect = request.form.get('File-Dropdown')
        filePath = ""
        if fileSelect in csvFilesName:
            index = csvFilesName.index(fileSelect)
            filePath = csvFilesPos[index]


        data = extract_data(filePath)
        print(data,file=sys.stderr)
    return render_template('Visualisation.html',Arraynames = csvFilesName)


if __name__ == "__main__":
    app.run(debug=True)
