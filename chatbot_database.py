import sqlite3
import os

current_directory = os.getcwd()
data_directory = os.path.join(current_directory, 'data')

sqlite_transaction = [] 
connection = sqlite3.connect('{}.db'.format('my_db'))
c = connection.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS qNa(
        question TEXT PRIMARY KEY, answer TEXT
    )""")

if __name__ == "__main__":
    create_table()
    for file in os.listdir(data_directory):
        file_path =  os.path.join(data_directory, file)
        with open(file_path, buffering=1000, encoding='utf8') as f:
            read_data = f.read()
            print(read_data)
            print("\n" * 20)

        