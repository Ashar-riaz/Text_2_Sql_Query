import sqlite3

con=sqlite3.connect("automobile.db")
cursor=con.cursor()
data=cursor.execute('''Select * From car''')
for row in data:
    print(row)
con.commit()
con.close()