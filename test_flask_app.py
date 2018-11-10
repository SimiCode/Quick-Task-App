import unittest
from flask_app import app
import json


class TestRoutes(unittest.TestCase):
   
    def setUp(self):
        self.app = app.test_client()

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
        orders = json.loads(resp.data.decode())
        self.assertIsInstance(orders, list)
        self.assertIn('my taskest task', orders)



