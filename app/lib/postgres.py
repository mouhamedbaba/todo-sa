from os import getenv
from dotenv import load_dotenv
import psycopg2
import random
load_dotenv()


class Postgres():
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password=getenv('POSTGRES_PASSWORD'),
        ) 
        self.cursor = self.conn.cursor()
        
    def initdb(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                uid SERIAL PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                uuid INTEGER REFERENCES users(uid),
                title VARCHAR(255) NOT NULL,
                priority VARCHAR(255) NOT NULL,
                head_color VARCHAR(255) NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT NOW(),
                deadline TIMESTAMP 
            )
        """)
        self.conn.commit()
        
    
    def create_user(self, username, password):
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.conn.commit()
        except Exception as e:
            print(e)
        
    def get_user(self, username):
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
            return None
        
    def get_user_by_username_and_password(self, username, password):
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            row = self.cursor.fetchone()
            if row:
                columns = [desc[0] for desc in self.cursor.description]
                return dict(zip(columns, row))
            else:
                return None
        except Exception as e:
            print(e)
            return None

        
    def create_task(self, uid, title, priority, head_color, deadline=None, completed=False):
        try:
            self.cursor.execute("INSERT INTO tasks (uuid, title, priority, head_color, deadline, completed) VALUES (%s, %s, %s, %s, %s, %s)", (uid, title, priority, head_color, deadline, completed))
            self.conn.commit()
        except Exception as e:
            print(e)
    
    def get_tasks(self, uid):
        try:
            self.cursor.execute("SELECT * FROM tasks WHERE uuid = %s", (uid,))
            rows = self.cursor.fetchall()
            if rows:
                columns = [desc[0] for desc in self.cursor.description]
                tasks = []
                for row in rows:
                    task_dict = dict(zip(columns, row))
                    tasks.append(task_dict)
                return tasks
            else:
                return None
        except Exception as e:
            print(e)
            return None
    
    def update_task(self, id, column, value):
        try:
            self.cursor.execute(f"UPDATE tasks SET {column} = %s WHERE id = %s", (value, id))
        except Exception as e:
            print(e)   
    
    def delete_task(self, id):
        try:
            self.cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
            self.conn.commit()
        except Exception as e:
            print(e)

    
    def close(self):
        self.conn.close()
        
    def __del__(self): 
        self.close()
        
postgres = Postgres()
postgres.initdb()
def add_random_tasks():
    for i in range(10):
        postgres.create_task(1, f'Task {i}', random.choice(['low', 'medium', 'high']), random.choice(['red', 'green', 'blue']), random.choice([True, False]))

# add_random_tasks()