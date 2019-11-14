import sqlite3
conn= sqlite3.connect("site.db")
cursor= conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user( id INTEGER  )")
conn.commit()
conn.close()