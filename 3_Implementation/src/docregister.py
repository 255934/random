# pylint: disable=C0301,C0114,C0116,C0121,C0103,R0914,R0913,C0303,C0200,W0622,R1710
import sqlite3
from sys import exit


def doctor_details():
    connection = sqlite3.connect("project.db")

    cursor = connection.cursor()
    doctor = """CREATE TABLE IF NOT EXISTS
    doctors(D_id INTEGER PRIMARY KEY, name CHAR(30) NOT NULL, SPECIALIZATION 
    CHAR(30) NOT NULL, H_id INT NOT NULL, Address CHAR(30) NOT NULL,PHONE INT UNIQUE,
     AADHAAR INT UNIQUE, password  )"""
    cursor.execute(doctor)
    connection.commit()
    connection.close()

    print("\n***** MANAGE DOCTORS - Here You Can Add,Delete,Update and View Doctor Details *****\n")
    print("1 : ADD DOCTOR")
    print("2 : Delete Doctor")
    print("3 : Update Doctor Details")
    print("4 :View doctors")
    print("5 : Admin Logout")
    admin_choice = int(input("Enter Your Choice: "))

    if admin_choice == 1:
        conn = sqlite3.connect("project.db")
        cur = conn.cursor()
        cur.execute("select hospital_license_no,hospital_name from hospitalDetails")
        view_hospitals = cur.fetchall()
        print("Hospital-Id\t Hospital-name\t")
        for i in range(len(view_hospitals)):
            print("\n")
            for j in range(len(view_hospitals[i])):
                print(str(view_hospitals[i][j]) + "\t\t", end=" ")
            print("\n")
        print("* NOTE - DOCTOR MUST BE FROM THE ABOVE LIST OF HOSPITAL ONLY")
        doctorlicno = int(input("Enter Licence NO: "))
        docname = input("Name:")
        area = input("Specialization: ")
        phone = int(input("Phone Number: "))
        hospitallicno = int(input("Hospital Licence Number: "))
        address = input("Address: ")
        aadhaar = int(input("Aadhaar Number:"))
        pwd = input("Enter Password: ")
        add_doctor(doctorlicno, docname, area, hospitallicno, address, phone, aadhaar, pwd)

    elif admin_choice == 2:
        remove = int(input("Enter Doctor Id you wat to delete: "))
        drop_doctor(remove)
    elif admin_choice == 3:
        i_d = int(input("enter doc_id You want to update: "))
        edit_doctor(i_d)
    elif admin_choice == 4:
        view_doctor()
    elif admin_choice == 5:
        print("Admin LoggedOut !!")
        exit()
    else:
        print("Wrong Choice - TRY AGAIN")
        doctor_details()


def add_doctor(doctorlicno, docname, area, hospitallicno, address, phone, aadhaar, pwd):
    try:
        conn = sqlite3.connect("project.db")
        cur = conn.cursor()
        cur.execute("select hospital_license_no from hospitalDetails")
        added = cur.fetchall()
        hid = []
        for i in range(len(added)):
            for j in range(len(added[i])):
                hid.append(added[i][j])
        if str(hospitallicno) not in hid:
            print("Oops! - Invalid Hospital Id")
            return -1

        # check if length of each input if valid or not
        if len(str(doctorlicno)) != 8 | len(str(hospitallicno)) != 8 | len(str(phone)) != 10 | len(
                str(aadhaar)) != 12 | len(pwd) != 8:
            print(" Error ---> ", end="")
            print(""" DoctorID Must be 8 characters,password 8 characters,HospitalId 8 characters,
             Phone 10 digits, Aadhar 12 digits""")
            return -1
        insert = """insert into doctors (D_id, name, SPECIALIZATION, H_id, Address, 
        PHONE, AADHAAR,password) values(?,?,?,?,?,?,?,?) """
        cur.execute(insert, (doctorlicno, docname, area, hospitallicno, address, phone, aadhaar, pwd))
        # cur.execute("select * from doctors")
        # print(cur.fetchall())
        print("Added successfully")
        conn.commit()
        conn.close()
        return 1
    except sqlite3.Error as error:
        print("Failed to Add record", error)
        return -1


def drop_doctor(remove):
    if not id_check(remove):
        print("\n *-- User Doesn't exist --*")
        return -1
    try:
        conn = sqlite3.connect("project.db")
        cur = conn.cursor()
        delete_doc = "delete from doctors where D_id=?"
        cur.execute(delete_doc, (remove,))
        print("Successfully Deleted")
        conn.commit()
        conn.close()
        return 1

    except sqlite3.Error as error:
        print("Failed to Delete record", error)
        return -1


def edit_doctor(i_d):
    # check whether user exists or not
    if id_check(i_d):
        print("Note: Phone number, aadress, password, Hospital id are the only things can be updated")
        print("1 : Phone Number")
        print("2 : Address")
        print("3 : Password")
        print("4 : Hospital_Id")
        conn = sqlite3.connect("project.db")
        cur = conn.cursor()
        admin_choice = int(input("Enter Your Choice: "))
        if admin_choice == 1:
            new_phone = input("Enter new phone Number: ")
            cur.execute("update doctors set PHONE=? where D_id=?", (new_phone, i_d))
            print("Successfully Updated")
            conn.commit()
            doctor_details()

        elif admin_choice == 2:
            new_address = input("Enter new phone Number: ")
            cur.execute("update doctors set Address=? where D_id=?", (new_address, i_d))
            print("Successfully Updated")
            conn.commit()
            doctor_details()
        elif admin_choice == 3:
            new_password = input("Enter new phone Number: ")
            confirm = input("Re-enter new password")
            if new_password == confirm:
                cur.execute("update doctors set password=? where D_id=?", (new_password, i_d))
                print("Successfully Updated")
                conn.commit()
                doctor_details()
            else:
                print("Update Failed")
                print("newpassword and confirm password must be same")
                exit()
        elif admin_choice == 4:
            new_hid = input("Enter new phone Number: ")
            cur.execute("update doctors set H_id=? where D_id=?", (new_hid, i_d))
            print("Successfully Updated")
            conn.commit()
            doctor_details()

        else:
            print("Wrong Choice - TRY AGAIN")
            doctor_details()

    else:
        print("\n *-- User Doesn't exist --*")
        exit()


def view_doctor():
    conn = sqlite3.connect("project.db")
    cur = conn.cursor()
    cur.execute("select D_id,H_id,name,SPECIALIZATION from doctors")
    added = cur.fetchall()
    print("Doctor-Id\t Hospital-Id\t DoctorName\t SPECIALIZATION\t")
    for i in range(len(added)):
        for j in range(len(added[i])):
            print(str(added[i][j]) + "\t\t", end=" ")
        print("\n")
    return 1


def id_check(remove):
    conn = sqlite3.connect("project.db")
    cur = conn.cursor()
    # check whether user exists or not
    cur.execute("select * from doctors where D_id=? ", (remove,))
    check_id_exist = len(cur.fetchall())
    if check_id_exist != 0:
        return True
