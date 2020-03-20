import sqlite3

def insert_columns_and_rows():
        d ={}
        for i in range(100):
            column =input("if you want to close type close or enter a column deatils:")
            
            if column.lower() == 'close':
                break
            row =input("enter a row deatils:")
            if column not in d:
                d[column] = []
		#print(d)
                d[column].append(row)
            else:
                d[column].append(row)
        print(d)
	
if __name__ == "__main__":
        insert_columns_and_rows()
                
       
