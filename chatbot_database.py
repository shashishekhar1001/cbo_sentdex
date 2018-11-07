import sqlite3
import os
import ruamel.yaml as yaml

current_directory = os.getcwd()
data_directory = os.path.join(current_directory, 'data')

sqlite_transaction = [] 
connection = sqlite3.connect('{}.db'.format('my_db'))
c = connection.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS qNa(
        question TEXT, answer TEXT
    )""")

if __name__ == "__main__":
    create_table()
    test_done = False
    for file in os.listdir(data_directory):
        file_path =  os.path.join(data_directory, file)
        with open(file_path, buffering=1000, encoding='utf8') as stream:
            try:
                my_dict = yaml.safe_load(stream)
                if not test_done:
                    for item in my_dict['conversations']:
                        with open("test.from", "a", encoding='utf8') as f:
                            f.write(item[0] + '\n')
                        with open("test.to", "a", encoding='utf8') as f:
                            f.write(item[1] + '\n')
                    test_done = True
                else:
                    for item in my_dict['conversations']:
                        with open("train.from", "a", encoding='utf8') as f:
                            f.write(item[0] + '\n')
                        with open("train.to", "a", encoding='utf8') as f:
                            f.write(item[1] + '\n')
            except yaml.YAMLError as exc:
                print(exc)

        