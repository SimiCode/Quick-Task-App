from flask import Flask, request, jsonify
import models


app = Flask(__name__)


@app.route('/api/v1/tasks')
def get_all_tasks():
	tasks = models.get_tasks()
	return jsonify(tasks), 200

@app.route('/api/v1/tasks', methods=['POST'])
def add_an_order():
	data = request.get_json()
	task = data.get('name')
	models.add_oder(task)
	return "success", 201


if __name__ == '__main__':
	app.run(debug=True)