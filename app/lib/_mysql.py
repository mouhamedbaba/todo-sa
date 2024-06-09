from os import getenv
from dotenv import load_dotenv
import mysql.connector
import random
import requests
load_dotenv()


class Mysql():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            database="todolist",
            user="mbl",
            password=getenv('MYSQL_PASSWORD'),
        ) 
        self.cursor = self.conn.cursor()
        
    def initdb(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                uid SERIAL PRIMARY KEY,
                name VARCHAR(250),
                username VARCHAR(255) UNIQUE NOT NULL,
                email VARCHAR(250) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,     
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                uuid INTEGER REFERENCES users(uid),
                title VARCHAR(255) NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT NOW()
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
            print(username, password)
            self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            row = self.cursor.fetchone()
            print("row : ", row)
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
            self.cursor.execute("SELECT * FROM tasks WHERE uuid = %s ORDER BY created_at DESC", (uid,))
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


mysqldb = Mysql()
mysqldb.initdb()

# # res = requests.get("https://jsonplaceholder.typicode.com/users")
# res = requests.get("https://jsonplaceholder.typicode.com/todos")
# # users = res.json()
# todos = res.json()
 




# print(len(users))
# # for user in users :
# #     print(user)
# #     usename = user.get("username")
# #     pw = f"{usename}pass".lower()
# #     values = (user.get("id"), user.get("name"), usename, user.get("email"), pw)
# #     mysqldb.cursor.execute("""
# #     INSERT INTO users(uid, name, username, email, password) VALUES (%s, %s, %s, %s, %s)
# # """, values)
# #     mysqldb.conn.commit()
# #     print(f"{usename} added")


                # id SERIAL PRIMARY KEY,
                # uuid INTEGER REFERENCES users(uid),
                # title VARCHAR(255) NOT NULL,
                # completed BOOLEAN NOT NULL DEFAULT FALSE,
                # created_at TIMESTAMP DEFAULT NOW()

# for todo in todos :
#     values = (todo.get("id"), todo.get("userId"), todo.get("title"), todo.get("completed"))
#     mysqldb.cursor.execute("""
#     INSERT INTO tasks(id, uuid, title, completed) VALUES (%s, %s, %s, %s)
# """, values)
#     mysqldb.conn.commit()
#     print(todo.get("title"), "added")   