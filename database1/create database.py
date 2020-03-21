import sqlite3


def create_database():
    dbname=input("enter a database name:")
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    conn.commit()
    print("DB Connected successfully database successfully")
    close_database = input("if you want to close database type close or enter a create_table type create : ")
    if conn == 'close' :
        conn.close()
    if conn == 'create':
        create_table()


if __name__ == "__main__":
    create_database()
