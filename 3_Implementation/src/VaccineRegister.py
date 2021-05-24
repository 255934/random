import sqlite3
import re
from datetime import datetime
connection = sqlite3.connect('../project.db')
cursor = connection.cursor()


def check_date(DATE):
    try:
        day, month, year = DATE.split("/")
    except ValueError:
        return 1  # Incorrect Date Format.
    else:
        try:
            today = datetime.today()
            today = datetime(today.year, today.month, today.day, 0, 0, 0)
            req_date = datetime(int(year), int(month), int(day))
            if today == req_date:
                return 2  # today's date
            else:
                return 3  # Not today's date
        except ValueError:
            return 4  # Invalid Date.


def check_available(hospital_id):
    sql = 'select * from VACCINE where hospital_id = ?'
    cursor.execute(sql, (hospital_id,))
    d = cursor.fetchall()
    if 0 <= len(d) < 30:
        return 5
    else:
        return 6


def check_doctor_id(doctor_id, hospital_id):
    cursor.execute("SELECT CASE WHEN EXISTS(SELECT * FROM doctors WHERE D_id = ?) THEN '1' ELSE '0' END",
                   (doctor_id, ))
    doc_flag = cursor.fetchall()
    if doc_flag[0][0] == '1':
        sql = '''SELECT CASE WHEN EXISTS(SELECT * FROM doctors WHERE D_id = ? AND H_id = ?)
         THEN '1' ELSE '0' END'''
        cursor.execute(sql, (doctor_id, hospital_id))
        h_flag = cursor.fetchone()
        if h_flag[0] == '1':
            return 7  # Success, doctor & hospital exists.
        else:
            return 8  # Fail, doctor exists but hospital mismatch.
    else:
        return 9  # Fail, doctor itself does not exist.


def check_mobile_number(mobile_number):
    if len(mobile_number) != 10:
        return 10
    pattern = r"[7-9][0-9]{9}"
    if not re.match(pattern, mobile_number):
        return 11  # Mobile number valid

    sql = "SELECT CASE WHEN EXISTS(SELECT * FROM usertable WHERE mobile=?) THEN '1' ELSE '0' END"
    cursor.execute(sql, (mobile_number, ))
    valid = cursor.fetchone()
    if valid[0] == 1:
        return 12  # Present in user table
    else:
        return 13  # Not present in user table


def patient_details(HOSPITAL_ID, DOCTOR_ID, PATIENT_NAME, PATIENT_AGE, DATE, MOBILE_NUMBER, GENDER):
    valid_mobile_no = check_mobile_number(MOBILE_NUMBER)
    if valid_mobile_no == 12:
        valid_date = check_date(DATE)
        if valid_date == 2:
            valid_doctor = check_doctor_id(DOCTOR_ID, HOSPITAL_ID)
            if valid_doctor == 7:
                available = check_available(HOSPITAL_ID)
                if available == 5:
                    sql = 'INSERT INTO VACCINE VALUES(?,?,?,?,?,?,?)'
                    cursor.execute(sql,
                                   (HOSPITAL_ID, DOCTOR_ID, PATIENT_NAME, PATIENT_AGE, DATE, MOBILE_NUMBER, GENDER))
                    connection.commit()
                    # Default fee for Vaccine booking is 500
                    # Payment() is in Uday's code.
                    fail, success = Payment(PATIENT_NAME, 500, MOBILE_NUMBER)
                    if fail:
                        sql = "DELETE FROM APPOINTMENT WHERE mobile=?"
                        cursor.execute(sql, (MOBILE_NUMBER,))
                        connection.commit()
                    return 20
                else:
                    return available
            else:
                return valid_doctor
        else:
            return valid_date
    else:
        return valid_mobile_no


connection.close()