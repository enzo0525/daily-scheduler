from flask import Flask, request, render_template, jsonify, redirect, url_for
from database import add_task_database, get_all_routines

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.j2")

@app.route('/routines', methods=['GET'])
def routines():
    return render_template('routines.j2')

@app.route('/api/routines', methods=['GET'])
def api_routines():
    routines = get_all_routines()

    for routine in routines:
        routine['_id'] = str(routine['_id']) #Transforming _id to string, error appears if not (JSON cannot be serialized)

    return jsonify(routines)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = {
            'taskName': request.form['taskName'],
            'taskDayOfWeek': request.form['taskDayOfWeek'],
            'taskNotes': request.form['taskNotes']
        }

        #add error handling (no name)

        add_task_database(data)
        return render_template('submit.j2')
    
if __name__ == '__main__':
    app.run(debug=True)