# pylint: disable=C0103,C0114
import sqlite3

conn = sqlite3.connect('../project.db')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())
c.execute("select sql from sqlite_master where name='duetable'")
print(c.fetchall())
conn.commit()
conn.close()
