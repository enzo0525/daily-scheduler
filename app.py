from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        print(request.form['taskName'], request.form['taskDate'], request.form['taskNotes'])
        return render_template('submit.html')
    