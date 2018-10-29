import sqlite3

sqlite_transaction = [] 
connection = sqlite3.connect('{}.db'.format('my_db'))
c = connection.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS qNa(
        question TEXT PRIMARY KEY, answer TEXT
    )""")


if __name__ == "__main__":
    create_table()