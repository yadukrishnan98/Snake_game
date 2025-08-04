import sqlite3


CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS Users(user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                name TEXT,
                                                score INTEGER,
                                                high_score INTEGER)'''



class Database():

    def __init__(self):
        self.conn = sqlite3.connect('sample.db')
        self.cur = self.conn.cursor()
        self.create_table()


    def create_table(self):
        self.cur.execute(CREATE_TABLE)

    
    def insert_row(self, name, score, high_score):
        insert_script = f'''INSERT INTO Users(name, score, high_score) VALUES(?, ?, ?)'''
        self.cur.execute(insert_script, (name, score, high_score))
        self.conn.commit()

    
    def top_scores(self):
        query = '''SELECT name, score FROM Users ORDER BY score DESC LIMIT 5'''
        self.cur.execute(query)
        results = self.cur.fetchall()
        return results


    def close(self):
        if self.conn:
            self.conn.close()



db_con = Database()