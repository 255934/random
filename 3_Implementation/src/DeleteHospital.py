import sqlite3

conn = sqlite3.connect('project.db')
c = conn.cursor()


def hospital_delete(hospital_license_no):
    if len(hospital_license_no) < 8:
        print("License Number Entered should be of 8 digits, Entered number less than 8 digits")
        return 0
    if len(hospital_license_no) > 8:
        print("License Number Entered should be of 8 digits, Entered number more than 8 digits")
        return 7
    if not hospital_license_no.isdecimal():
        print("License Number cannot have characters , should have only digits")
        return 1
    c.execute('select * from hospitalDetails where hospital_license_no = ?', (hospital_license_no,))
    d = c.fetchall()
    if len(d) == 0:
        print("record doesnt exist")
        return 13
    c.execute('DELETE FROM hospitalDetails WHERE hospital_license_no =?', (hospital_license_no,))

    conn.commit()

    return 100
