import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

for row in c.execute("SELECT * FROM requests"):
    print(row)

conn.close()