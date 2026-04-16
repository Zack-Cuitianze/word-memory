import sqlite3

class Database:
    def __init__(self, db_name=':memory:'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY,
            value TEXT NOT NULL
        )''')
        self.connection.commit()

    def insert_data(self, value):
        self.cursor.execute('''INSERT INTO data (value) VALUES (?)''', (value,))
        self.connection.commit()

    def fetch_data(self):
        self.cursor.execute('''SELECT * FROM data''')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()