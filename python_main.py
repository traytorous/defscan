from flask import Flask, render_template, request, url_for, redirect
from werkzeug import secure_filename
import pprint
import subprocess
import os

def scan_file():
   x = subprocess.getstatusoutput('ls | grep .exe | grep .file')
   x = x[1]
   data = subprocess.getstatusoutput('clamscan '+str(x))
   docs = open("viral.html","w")
   docs.write(str(data))
   

app = Flask(__name__)
@app.route('/')
@app.route('/index')

def index():
    return render_template("index.html")
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/virus_scanner')
def virus():
    return render_template('virusscanner.html')

@app.route('/done', methods = ['GET', 'POST'])
def scanner():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
    scan_file()
    os.system("mv /var/www/html/viral.html /var/www/html/templates")
    return render_template("viral.html")


if __name__ == "__main__":
    app.run(port=80,host='0.0.0.0')
