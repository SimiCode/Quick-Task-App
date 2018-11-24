from flask import Flask, request, jsonify
from models import Tasks, User, users
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    username_table = {u.username: u for u in users}
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    userid_table = {u.id: u for u in users}
    user_id = payload['identity']
    return userid_table.get(user_id, None)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
tasks_db = Tasks()

jwt = JWT(app, authenticate, identity)


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    User(username, password)
    return "User Created", 201

@app.route('/')
def home():
    return "Welcome Back!"

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

@app.route('/api/v1/tasks')
def get_all_tasks():
    tasks = tasks_db.get_tasks()
    return jsonify(tasks), 200

@app.route('/api/v1/tasks', methods=['POST'])
def add_new_task():
    data = request.get_json()
    task = data.get('name')
    tasks_db.add_task(task)
    return "success", 201

@app.route('/cleardb')
def shutdown():
    tasks_db.clear_all()
    return "Erased DB Tables", 200




# I am registering for DataHack4FI to:
# - get access to Microsoft Data Science education and level up my skill-set
# - meet fellow data enthusiasts from Africa, share and learn together.
# - learn in a co-motivational environment with a chance of landing employment.
# - learn skills that I can use to solve social, developmental problems and answer tough questions (The Data driven approach)