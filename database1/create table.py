import sqlite3


def create_table():
    table = input("enter a table name : ")
    
    for i in table:
        
        create_table = input("if you want to close type close or create : ")
        if create_table.lower() == 'close':
            break
        if create_table == 'create':
            insert_columns_and_rows()

if __name__ == "__main__":
    create_table()
