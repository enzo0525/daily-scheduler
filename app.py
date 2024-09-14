from flask import Flask, render_template, request
from database import add_task_database

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/routines', methods=['GET'])
def routines_page():
    return render_template('routines.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = {
            'taskName': request.form['taskName'],
            'taskDayOfWeek': request.form['taskDayOfWeek'],
            'taskNotes': request.form['taskNotes']
        }

        add_task_database(data)
        return render_template('submit.html')