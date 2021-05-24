import sqlite3
# ../ added by Vinuthna.
conn = sqlite3.connect('../project.db')
c = conn.cursor()


def patient_visiting_hospital(hospital_license_no):
    if len(hospital_license_no) < 8:
        print("License Number Entered should be of 8 digits, Entered number less than 8 digits")
        return 0
    if len(hospital_license_no) > 8:
        print("License Number Entered should be of 8 digits, Entered number more than 8 digits")
        return 7
    if not hospital_license_no.isdecimal():
        print("License Number cannot have characters , should have only digits")
        return 1
    # Care of table name for appointment table and the column name for hospital_license_no
    c.execute('select * from APPOINTMENT where HOSPITAL_ID = ?', (hospital_license_no,))
    d = c.fetchall()
    if d == 0:
        print("No One is Visiting This hospital")
        return 8
    print("The number of people visiting", d)
    return 9
