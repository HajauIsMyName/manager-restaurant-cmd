import sqlite3


class DBHandler:
    def __init__(self, db_name="data.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def query(self, sql, params=()):
        self.cursor.execute(sql, params)
        return self.cursor

    def execute(self, sql, params=()):
        self.cursor.execute(sql, params)
        self.conn.commit()

    def close(self):
        self.conn.close()
