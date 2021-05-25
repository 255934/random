# pylint: disable=E0401,R0801,R0913, R1705,E0402,C0301,C0114,C0116,C0121,C0103
import sqlite3
import re
from datetime import datetime
import Hospital_payment_portal

connection = sqlite3.connect('project.db')
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
        return 10  # Mobile number invalid
    pattern = r"[7-9][0-9]{9}"
    if re.match(pattern, mobile_number):
        return 11  # Mobile number valid
    else:
        return 12  # Mobile number invalid


def patient_details(HOSPITAL_ID, DOCTOR_ID, PATIENT_NAME, PATIENT_AGE, DATE, MOBILE_NUMBER, GENDER):
    valid_mobile_no = check_mobile_number(MOBILE_NUMBER)
    if valid_mobile_no == 11:
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
                    fail = Hospital_payment_portal.Payment(MOBILE_NUMBER, 500, PATIENT_NAME)
                    if fail == 'Payment Failed':
                        sql = "DELETE FROM APPOINTMENT WHERE mobile=?"
                        cursor.execute(sql, (MOBILE_NUMBER,))
                        connection.commit()
                        print("Registration unsuccessful")
                        return -1
                    else:
                        print("Registration unsuccessful")
                        return 20
                else:
                    print("Slots unavailable")
                    return available
            else:
                print("Wrong Doctor ID or Hospital ID")
                return valid_doctor
        else:
            print("Invalid date")
            return valid_date
    else:
        print("Invalid Mobile number")
        return valid_mobile_no
