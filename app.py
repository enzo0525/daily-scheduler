from flask import Flask, request, render_template, jsonify
from database import add_task_database, get_all_routines, remove_task_database

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

        add_task_database(data)
        return render_template('submit.j2')
    
@app.route('/api/routines/delete/<string:routine_id>', methods=['DELETE'])
def api_routines_delete(routine_id):
    if remove_task_database(routine_id):
        return jsonify({'message': 'OK'}), 200
    return jsonify({'message': 'ERROR'}), 404
    
if __name__ == '__main__':
    app.run(debug=True)