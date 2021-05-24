import sqlite3

conn = sqlite3.connect('../project.db')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

conn.commit()
conn.close()
