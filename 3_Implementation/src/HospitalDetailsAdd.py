# pylint: disable=R0911,R0912,R0913,C0301,C0114,C0116,C0121,C0103
import sqlite3
import re
conn = sqlite3.connect('project.db')
c = conn.cursor()


def hospital_add(hospital_license_no, hospital_name, hospital_foundation_date, hospital_appointment_cost,
                 hospital_contact, hospital_email_id, hospital_address):
    # check if license no is of 8 digits
    if len(hospital_license_no) < 8:
        print("License Number Entered should be of 8 digits, Entered number less than 8 digits")
        return 0
    if len(hospital_license_no) > 8:
        print("License Number Entered should be of 8 digits, Entered number more than 8 digits")
        return 7
    if not hospital_license_no.isdecimal():
        print("License Number cannot have characters , should have only digits")
        return 1
    # check if hospital name meets the constraint
    if len(hospital_name) < 3:
        print("Name of Hospital cannot be less than 3 characters")
        return 2
    if len(hospital_name) > 20:
        print("Name of Hospital cannot be more than 20 characters")
        return 3
    if not hospital_name.isalpha():
        print("Hospital name should only have alphabets")
        return 4
    # check if foundation date is in format of yyyy-mm-dd

    if not hospital_appointment_cost.isdecimal():
        print("cost should have only digits")
        return 6
    if len(hospital_contact) < 10:
        print("Number Entered should be of 10 digits")
        return 8
    if len(hospital_contact) > 10:
        print("License Number Entered should be of 8 digits, Entered number more than 8 digits")
        return 9
    if not hospital_contact.isdecimal():
        print("License Number cannot have characters , should have only digits")
        return 10
    regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if not re.search(regex, hospital_email_id):
        print(" Email format not matched")
        return 11
    if len(hospital_address) <= 10:
        print("Invalid address , should be more than 10 characters")
        return 12

    c.execute('select * from hospitalDetails where hospital_license_no = ?', (hospital_license_no,))
    d = c.fetchall()
    if len(d) != 0:
        print("license Number already exists")
        return 13

    c.execute('INSERT INTO hospitalDetails VALUES (?,?,?,?,?,?,?)', (hospital_license_no, hospital_name,
                                                                     hospital_foundation_date, hospital_appointment_cost
                                                                     , hospital_contact, hospital_email_id,
                                                                     hospital_address))

    conn.commit()

    return 100
