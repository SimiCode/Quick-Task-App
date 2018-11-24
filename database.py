import os
import psycopg2
import psycopg2.extras


class DatabaseConnection:

    def __init__(self):
        if os.getenv('APP_SETTINGS') == 'test_db':
            self.db_name = 'test_db'
        else:
            self.db_name = 'd8qb27bt4r07nf'
                
        db_credentials = f"""
        dbname='{self.db_name}' user='foznymlisghlyh' password='e60937bf246a4e62e2ac4b7135d4c291dd61c98066c84d2d89d38ac0a2400f53'
        host='ec2-50-19-249-121.compute-1.amazonaws.com' port='5432'
        """
        # connect to the database
        connection = psycopg2.connect(dbname=self.db_name, user='edison', password='password', host='localhost', port='5432')
        connection.autocommit = True
        self.cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        print(self.cursor)

        # create the tables
        create_task_table = "CREATE TABLE IF NOT EXISTS tasks (taskID BIGSERIAL NOT NULL PRIMARY KEY, task TEXT NOT NULL);"
        self.cursor.execute(create_task_table)

    def get_db_tasks(self):
        sql_command = """
        select * from tasks;
        """
        self.cursor.execute(sql_command)
        rows = self.cursor.fetchall()
        return rows

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
