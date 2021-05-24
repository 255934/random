import sqlite3
connection = sqlite3.connect("../../3_Implementation/project.db")
cursor = connection.cursor()
doctor = """CREATE TABLE IF NOT EXISTS
doctors(D_id INTEGER PRIMARY KEY, name VARCHAR(30) NOT NULL, SPECIALIZATION 
VARCHAR(30) NOT NULL, H_id INT NOT NULL, Address VARCHAR(30) NOT NULL,PHONE INT UNIQUE,
 AADHAAR INT UNIQUE, password  )"""
cursor.execute(doctor)
connection.commit()
connection.close()