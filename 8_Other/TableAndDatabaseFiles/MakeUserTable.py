## pylint: disable=C0102,C0114,C0103
import sqlite3
connection = sqlite3.connect("../../3_Implementation/project.db")
cursor = connection.cursor()
user = """CREATE TABLE IF NOT EXISTS
user(name, age, ph_no, userid, password, aadhaar)"""
cursor.execute(user)
connection.commit()
connection.close()
