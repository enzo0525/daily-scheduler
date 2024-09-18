from flask import Flask, request, render_template, jsonify
from database import add_task_database, get_all_routines, remove_task_database

app = Flask(__name__)

@app.route('/', methods=['GET']) #Index route.
def index():
    return render_template("index.j2"), 200

@app.route('/routines', methods=['GET']) #Routines route.
def routines():
    if get_all_routines():
        return render_template('routines.j2'), 200
    return render_template('routines.j2', message='No routines were found, try adding some!'), 500

@app.route('/api/routines', methods=['GET']) #GET requesting all data from database.
def api_routines():
    routines_list = get_all_routines()
    return jsonify(routines_list)

@app.route('/submit', methods=['POST']) #POST submitting data to insert in database.
def submit():
    data = {
        'taskName': request.form['taskName'],
        'taskDayOfWeek': request.form['taskDayOfWeek'],
        'taskNotes': request.form['taskNotes']
    }

    if add_task_database(data):
        return render_template('submit.j2', message='Task added succesfully!'), 200
    return render_template('submit.j2', message='There was an issue saving your task. Try again later.'), 500
    
@app.route('/api/routines/delete/<string:routine_id>', methods=['DELETE']) #DELETE removing data with routine_id from database.
def api_routines_delete(routine_id):
    if remove_task_database(routine_id):
        return jsonify({'message': 'OK'}), 200
    return jsonify({'message': 'ERROR'}), 500
    
if __name__ == '__main__':
    app.run(debug=True)