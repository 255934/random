# pylint: disable=C0301,C0114,C0116,C0121,C0103,R0914,R0913,C0303,C0200,W0622,R1710
import sqlite3

connection = sqlite3.connect("../../3_Implementation/project.db")
cursor = connection.cursor()
# DID - 8 digits, HID - 8 digits

# cursor.execute("DROP TABLE APPOINTMENT")
# connection.commit()

sql = '''CREATE TABLE IF NOT EXISTS APPOINTMENT(
    MOBILE TEXT PRIMARYKEY,
    DOCTOR_ID INTEGER NOT NULL,
    HOSPITAL_ID INT NOT NULL,
    DATE VARCHAR(15) NOT NULL,
    SYMPTOMS VARCHAR(200) NOT NULL,
    APPOINTMENT_TIME VARCHAR(15) NOT NULL,
    BOOKING_TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP
)'''
cursor.execute(sql)
connection.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# cursor.execute("SELECT sql FROM sqlite_master WHERE name='APPOINTMENT';")
# print(cursor.fetchall())

# Record inserted for Hanumantha Reddy
# cursor.execute("INSERT INTO APPOINTMENT( MOBILE, DOCTOR_ID, HOSPITAL_ID, DATE, SYMPTOMS, APPOINTMENT_TIME) VALUES('9004088473', 12345678, 87654321, '17/10/2021', 'Cough', '8 00')")
# connection.commit()

# Record inserted for Hanumantha Reddy
# cursor.execute("INSERT INTO APPOINTMENT( MOBILE, DOCTOR_ID, HOSPITAL_ID, DATE, SYMPTOMS, APPOINTMENT_TIME) VALUES('9877456321', 12345678, 12345698, '17/10/2021', 'Cough', '8 30')")
# connection.commit()

# Record inserted for Hanumantha Reddy
# cursor.execute("INSERT INTO APPOINTMENT( MOBILE, DOCTOR_ID, HOSPITAL_ID, DATE, SYMPTOMS, APPOINTMENT_TIME) VALUES('9632587436', 36985214, 12345678, '17/10/2021', 'Fever', '9 30')")
# connection.commit()

# Record inserted for Milan
# cursor.execute("INSERT INTO APPOINTMENT( MOBILE, DOCTOR_ID, HOSPITAL_ID, DATE, SYMPTOMS, APPOINTMENT_TIME) VALUES('9004088473', 12345679, 12345678, '17/10/2021', 'Fatigue', '13 00')")
# connection.commit()

cursor.execute("SELECT * FROM APPOINTMENT")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()
