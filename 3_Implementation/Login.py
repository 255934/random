import sqlite3
from src import HospitalDetailsAdd
from src import DeleteHospital
from src import HospitalDisplayPatient
from src import docregister
from src import Hospital_payment_portal
from src import book_appointment
from src import VaccineRegister
from src import doctorPortal

conn = sqlite3.connect('project.db')
c = conn.cursor()


def admin_menu():
    print("1. Hospital 2.Doctor 3. Appointments and patients")
    choice = int(input())
    if choice == 1:
        print("1. Add Hospital 2. Delete Hospital 3. View Patient visiting that hospital")
        choice2 = int(input())
        if choice2 == 1:
            print("License_no")
            hospital_license_no = input()
            print("Hospital Name")
            hospital_name = input()
            print("Foundation Date")
            hospital_foundation_date = input()
            print("Appointment Cost")
            hospital_appointment_cost = input()
            print("ContactNumber")
            hospital_contact = input()
            print("Email_id")
            hospital_email_id = input()
            print("Address more than 10 character")
            hospital_address = input()
            HospitalDetailsAdd.hospital_add(hospital_license_no, hospital_name, hospital_foundation_date,
                                            hospital_appointment_cost,
                                            hospital_contact, hospital_email_id, hospital_address)
        if choice2 == 2:
            print("License_no")
            hospital_license_no = input()
            DeleteHospital.hospital_delete(hospital_license_no)
        if choice2 == 3:
            print("License_no")
            hospital_license_no = input()
            HospitalDisplayPatient.patient_visiting_hospital(hospital_license_no)
    if choice == 2:
        docregister.doctor_details()
    if choice == 3:
        doctorPortal.doctor_portal()


def user_menu():
    print("1.BookDoctorAppointment 2. Vaccine")
    choice = int(input())
    if choice == 1:
        print("mobile")
        mobile = input()
        print("Doctor Id")
        doctor_id = input()
        print("Hospital Id")
        hospital_id = input()
        print("date")
        date = input()
        print("symptom")
        symptom = input()
        # appointment_time added by Vinuthna.
        print("Appointment Time(hh mm)")
        appointment_time = input()
        book_appointment.book_appointment(mobile, doctor_id, hospital_id, date, symptom, appointment_time)
    if choice == 2:
        print("HOSPITAL_ID")
        HOSPITAL_ID = input()
        print("DOCTOR_ID")
        DOCTOR_ID = input()
        print("Patient name")
        PATIENT_NAME = input()
        print("Patient age")
        PATIENT_AGE = input()
        print("date")
        DATE = input()
        print("Mobile")
        MOBILE_NUMBER = input()
        print("Gender")
        GENDER = input()
        VaccineRegister.patient_details(HOSPITAL_ID, DOCTOR_ID, PATIENT_NAME, PATIENT_AGE, DATE, MOBILE_NUMBER, GENDER)


def login():
    print("1. Login")
    print("2. Register")
    n = int(input())
    if n == 1:
        print("Enter UserId")
        user_id = input()
        print("Enter Password")
        password = input()
        if user_id == "admin" and password == "admin":
            admin_menu()
            return 0

        c.execute("select * from user where userid=? and password=?", (user_id, password))
        d = c.fetchall()
        if len(d) == 0:
            print("invalid details")
            return 0
        # Below statement by Vinuthna
        conn.close()
        user_menu()

    if n == 2:
        print("Enter Name")
        name = input()
        print("Enter age")
        age = int(input())
        print("Enter Phone Number:")
        ph_no = input()
        print("user id")
        userid = input()
        print("password")
        password = input()
        print("aadhaar")
        aadhaar = input()
        c.execute("INSERT INTO user VALUES (?,?,?,?,?,?)", (name, age, ph_no, userid, password, aadhaar))
        conn.commit()
        conn.close()


login()
