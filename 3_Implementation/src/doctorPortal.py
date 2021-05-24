# pylint: disable=C0301,C0114,C0116,C0121,C0103,R0914,R0913,C0303,C0200,W0622,R1710
import sqlite3

connection = sqlite3.connect("project.db")
cursor = connection.cursor()


def doctor_portal():
    print(" MANAGE APPOINTMENTS HERE")
    print("1: View Appointments")
    print("2: Sort Patients")
    doctor_id = int(input("Enter Doctor ID: "))
    if doc_check(doctor_id):
        user_choice = int(input("Enter choice: "))
        if user_choice == 1:
            doc = doctor_id
            view_appointments(doc)
        elif user_choice == 2:
            patient_mobile = input("Enter patient Mobile number: ")
            if check_mobile(patient_mobile):
                sort_patients(patient_mobile)
            else:
                print("Mobile Number is Not Registered !!")
                return 0
    else:
        print("Invalid Doctor_ID")
        return 0


def view_appointments(doc):
    view = "select * from APPOINTMENT where DOCTOR_ID=? order by APPOINTMENT_TIME desc"
    cursor.execute(view, (doc,))
    fetched_appointments = cursor.fetchall()
    print("APPOINTMENTS :")
    print("MOBILE\t\t DOCTOR_ID\t\t HOSPITAL_ID\t\t SYMPTOMS\t\t DATE\t\t APPOINTMENT_TIME\t\t BOOKED_ON\t\t")
    for i in range(len(fetched_appointments)):
        for j in range(len(fetched_appointments[i])):
            print(str(fetched_appointments[i][j]) + "\t\t", end=" ")
        print("\n")


def doc_check(doc):
    cursor.execute("select * from doctors where D_id=? ", (doc,))
    check_id_exist = len(cursor.fetchall())
    if check_id_exist != 0:
        return True

def sort_patients(mobile):
    view = "select name,age,ph_no,userid,aadhaar from user where ph_no=?"
    cursor.execute(view, (mobile,))
    fetched_patient = cursor.fetchall()
    print("Patient details")
    print("Name\t\t Age\t\t MobileNo\t\t UserId\t\t Aadhaar\t\t")
    for i in range(len(fetched_patient)):
        for j in range(len(fetched_patient[i])):
            print(str(fetched_patient[i][j]) + "\t\t", end=" ")
        print("\n")


def check_mobile(mobile):
    cursor.execute("select * from user where ph_no=? ", (mobile,))
    check_id_exist = len(cursor.fetchall())
    if check_id_exist != 0:
        return True
