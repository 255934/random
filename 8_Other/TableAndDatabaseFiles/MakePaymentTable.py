# pylint: disable=C0114,C0103
import sqlite3
conn = sqlite3.connect('../../3_Implementation/project.db')
c = conn.cursor()
c.execute("""CREATE TABLE wallettable (name text, mobile text PRIMARY KEY, amount int)""")
c.execute("""CREATE TABLE upitable (name text, mobile text, upipin int, acc_balance int )""")
c.execute("""CREATE TABLE duetable (name text, mobile text, status int)""")

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())
conn.commit()
conn.close()
