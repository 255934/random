# pylint: disable=C0103,C0114
import sqlite3

conn = sqlite3.connect('../project.db')
c = conn.cursor()

c.execute("SELECT * FROM appointment;")
print(c.fetchall())

conn.commit()
conn.close()
