import sqlite3
connection = sqlite3.connect("../../3_Implementation/project.db")
cursor = connection.cursor()

doctor = """CREATE TABLE IF NOT EXISTS APPOINTMENT(
    MOBILE TEXT PRIMARYKEY,
    DOCTOR_ID INTEGER NOT NULL,
    HOSPITAL_ID INT NOT NULL,
    DATE VARCHAR(15) NOT NULL,
    SYMPTOMS VARCHAR(200) NOT NULL,
    APPOINTMENT_TIME VARCHAR(15) NOT NULL)"""
cursor.execute(doctor)
connection.commit()
connection.close()