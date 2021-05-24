import sqlite3
from datetime import datetime
from .Hospital_payment_portal import Payment

import re

connection = sqlite3.connect("project.db")
cursor = connection.cursor()


def check_date(date):
    try:
        day, month, year = date.split("/")
    except ValueError:
        return 4  # Incorrect Date Format.
    else:
        try:
            today = datetime.today()
            req_date = datetime(int(year), int(month), int(day))
            if today > req_date:
                return 5  # Date is not for future booking.
            else:
                return 6  # All good.
        except ValueError:
            return 7  # Invalid Date.


def check_mobile_no(mobile):
    if len(mobile) != 10:
        return 8
    pattern = r"[7-9][0-9]{9}"
    if not re.match(pattern, mobile):
        return 9  # Mobile number valid
    else:
        return 10  # Mobile number valid


def book_appointment(mobile, doctor_id, hospital_id, date, symptom, app_time):
    mobile_flag = check_mobile_no(mobile)
    if mobile_flag == 10:
        cursor.execute("SELECT CASE WHEN EXISTS(SELECT * FROM doctors WHERE D_id=?) THEN 'TRUE' ELSE 'FALSE' END",
                       (doctor_id,))
        doc_flag = cursor.fetchall()
        if doc_flag[0][0] == 'TRUE':
            sql = '''SELECT CASE WHEN EXISTS(SELECT * FROM doctors WHERE D_id=? AND H_id=?)
                 THEN 'TRUE' ELSE 'FALSE' END'''
            cursor.execute(sql, (doctor_id, hospital_id))
            h_flag = cursor.fetchone()
            if h_flag[0] == 'TRUE':
                date_flag = check_date(date)
                if date_flag == 6:
                    sql = "INSERT INTO APPOINTMENT( MOBILE, DOCTOR_ID, HOSPITAL_ID, DATE, SYMPTOMS,APPOINTMENT_TIME) VALUES(?, ?, ?, ?, ?,?)"
                    cursor.execute(sql, (mobile, doctor_id, hospital_id, date, symptom,app_time))
                    connection.commit()
                    # default fee = 200 for a general appointment.
                    sql = "SELECT name FROM user WHERE ph_no=?"
                    cursor.execute(sql, (mobile,))
                    data = cursor.fetchall()
                    name=''
                    for i in range(len(data)):
                        for j in range(len(data[i])):
                            name=data[i][j]
                    print(type(name))


                    pay_status = Payment(mobile, 200, name)
                    if pay_status == 'Payment Failed':
                        sql = "DELETE FROM APPOINTMENT WHERE mobile=?"
                        cursor.execute(sql, (mobile,))
                        connection.commit()
                    return 20
                else:
                    if date_flag == 4:
                        print("Incorrect Date Format")
                    elif date_flag == 5:
                        print("Wrong Date")
                    else:
                        print("Invalid Date")
                    return date_flag  # Returns 4, 5 or 7
            else:
                print("Doctor ID and Hospital ID mismatch")
                return 2  # Fail, doctor exists but hospital mismatch.
        else:
            print("Doctor ID does not exist")
            return 3  # Fail, doctor itself does not exist.
    else:
        if mobile_flag == 8:
            print("Mobile no. is less than 10 digits")
        else:
            print("Invalid Mobile No.")
        return mobile_flag  # Returns 8, 9


# book_appointment('9003436778', 12345678, 87654321, '02/08/2021', 'fever', '9 00')
