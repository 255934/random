import sqlite3

connection = sqlite3.connect("../project.db")
cursor = connection.cursor()

sql = ''' CREATE TABLE IF NOT EXISTS VACCINE(
            HOSPITAL_ID NUMBER PRIMARYKEY,
            DOCTOR_ID INTEGER,
            PATIENT_NAME VARCHAR(100),
            PATIENT_AGE INTEGER,
            DATE VARCHAR(20),
            MOBILE INTEGER,
            GENDER VARCHAR(20)
            )'''
cursor.execute(sql)
connection.commit()

# insert_details="""insert into VACCINE(HOSPITAL_ID,DOCTOR_ID,PATIENT_NAME,PATIENT_AGE,VACCINE_COUNT)
# values(123, 521,"SRI",21,30) """
# cursor.execute(insert_details)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

'''
cursor.execute("SELECT * FROM VACCINE")
rows = cursor.fetchall()
for row in rows:
    # print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],sep="\t\t")
    print(row)
'''
connection.close()
