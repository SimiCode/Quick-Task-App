import os
import psycopg2
import psycopg2.extras


class DatabaseConnection:

    def __init__(self):
        if os.getenv('APP_SETTINGS') == 'test_db':
            self.db = 'test_db'
        else:
            self.db = 'herokuapp'

        db_credentials = """
        dbname='herokuapp' user='edison' password='password'
        host='localhost' port='5432'
        """
        # connect to the database
        connection = psycopg2.connect(dbname=self.db, user='edison', password='password', host='localhost', port='5432')
        connection.autocommit = True
        self.cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        print(self.cursor)

        # create the table
        create_user_table = "CREATE TABLE IF NOT EXISTS tasks (taskID BIGSERIAL NOT NULL PRIMARY KEY, task TEXT NOT NULL);"
        self.cursor.execute(create_user_table)

    def get_all_tasks(self):
        sql_command = """
        select * from tasks;
        """
        self.cursor.execute(sql_command)
        rows = self.cursor.fetchall()
        return rows

    # def create_task(self, taskID, task ):
    def create_task(self, task ):
        sql_command = f" \
        INSERT INTO tasks (task) values ('{task}'); \
        "
        print(sql_command)
        self.cursor.execute(sql_command)
        rowcount = self.cursor.rowcount
        return rowcount

    def drop_tables(self):
        drop = "DROP TABLE tasks"
        self.cursor.execute(drop)
