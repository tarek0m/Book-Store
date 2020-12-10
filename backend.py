import sqlite3

class Database:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        data = self.cur.fetchall()
         
        return data

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("""SELECT * FROM book WHERE title=? COLLATE NOCASE
                                            OR author=? COLLATE NOCASE
                                            OR year=? COLLATE NOCASE
                                            OR isbn=? COLLATE NOCASE
        """, (title, author, year, isbn))
        data = self.cur.fetchall()
         
        return data

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
         
    def update(self, id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()    

    def __del__(self):
        self.conn.close() 