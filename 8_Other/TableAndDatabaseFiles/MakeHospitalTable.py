import sqlite3
conn = sqlite3.connect('../../3_Implementation/project.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS hospitalDetails (hospital_license_no , hospital_name, hospital_foundation_date, hospital_appointment_cost,
                 hospital_contact, hospital_email_id, hospital_address)""")
conn.commit()
conn.close()
