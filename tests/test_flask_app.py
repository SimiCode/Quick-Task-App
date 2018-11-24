import unittest
from flask_app import app, tasks_db
import json
from models import Tasks, User, users

#jwt, docs, testDb, es6

class TestRoutes(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.app = app.test_client()
        # tasks_db = Tasks()

    def test_index(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.decode(), "Welcome Back!")

    def test_create_task(self):
        resp = self.app.post(
            '/api/v1/tasks', 
            headers={'Content-Type':'application/json'}, 
            data=json.dumps({'name':'my taskest task'})
        )
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data.decode(), 'success')

    def test_task_added(self):
        resp = self.app.get('/api/v1/tasks')
        self.assertEqual(resp.status_code, 200)
        tasks = json.loads(resp.data.decode())
        self.assertIsInstance(tasks, list)
        # rows from database are a dictionary, convert them to a list by picking keys
        task_names = [ task['task'] for task in tasks ]
        print(task_names)
        self.assertIn('my taskest task', task_names)

    def test_db_used(self):
        self.assertIs(tasks_db.db.db_name, 'd8qb27bt4r07nf')
        self.assertIsNot(tasks_db.db.db_name, 'test_db')

    @classmethod
    def tearDownClass(self):
        self.app.get('/cleardb')


