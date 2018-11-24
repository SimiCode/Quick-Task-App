from database import DatabaseConnection

# create User model
users = []

class Tasks:
	def __init__(self):
		self.db = DatabaseConnection()
		# self.db.drop_tables()
		# tasks = []

	def get_tasks(self):
		return self.db.get_db_tasks()

	def add_task(self, task):
		self.db.create_task(task)
		# tasks.append(task)

	def clear_all(self):
		self.db.drop_tables()

class User:
    def __init__(self, username, password):
        self.id = len(users)+1
        self.username = username
        self.password = password
        # add new user to users list
        users.append(self)

    def __str__(self):
        return "User(id='%s')" % self.id





