import sqlite3
from src import HospitalDetailsAdd
from src import DeleteHospital
from src import HospitalDisplayPatient
from src import docregister
from src import Hospital_payment_portal
from src import book_appointment
from src import VaccineRegister


conn = sqlite3.connect('project.db')
c = conn.cursor()

def test_add():
    assert HospitalDetailsAdd.hospital_add("1234567", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 0
    assert HospitalDetailsAdd.hospital_add("123456789", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 7
    assert HospitalDetailsAdd.hospital_add("1234567a", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 1
    assert HospitalDetailsAdd.hospital_add("12345678", "BK", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 2
    assert HospitalDetailsAdd.hospital_add("12345678", "dasdssadasdsdasdassdsa", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 3
    assert HospitalDetailsAdd.hospital_add("12345678", "BKMS1", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 4

    assert HospitalDetailsAdd.hospital_add("12345678", "BKMS", "1999-11-19", "100a", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 6
    assert HospitalDetailsAdd.hospital_add("12345678", "BKMS", "1999-11-19", "100", "900408847", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 8
    assert HospitalDetailsAdd.hospital_add("12345678", "BKMS", "1999-11-19", "100", "90040884732", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 9
    assert HospitalDetailsAdd.hospital_add("12345678", "BKMS", "1999-11-19", "100", "900408847a", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 10
    assert HospitalDetailsAdd.hospital_add("12345678", "BKMS", "1999-11-19", "100", "9004088473", "BKMSgmail.com",
                        "dasdssadasdsdasdassdsa") == 11
    assert HospitalDetailsAdd.hospital_add("12345678", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdss") == 12
    assert HospitalDetailsAdd.hospital_add("12345600", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssdsasdasdsa") == 100

    assert HospitalDetailsAdd.hospital_add("12345600", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssdsasdasdsa") == 13


def test_delete():

    assert DeleteHospital.hospital_delete("1234567") == 0
    assert DeleteHospital.hospital_delete("123456789") == 7
    assert DeleteHospital.hospital_delete("1234567a") == 1
    assert DeleteHospital.hospital_delete("67350000") == 13
    assert DeleteHospital.hospital_delete("12345600") == 100


def test_display_patient():
    assert HospitalDisplayPatient.patient_visiting_hospital("1234567") == 0
    assert HospitalDisplayPatient.patient_visiting_hospital("123456789") == 7
    assert HospitalDisplayPatient.patient_visiting_hospital("1234567a") == 1
    # vinuthna will have to make sure that no entry in appointment with h_id==00000
    assert HospitalDisplayPatient.patient_visiting_hospital("00000000") == 8
    # vinuthna will have to make sure that there is atleast 1 entry in appointment with h_id==12345678
    assert HospitalDisplayPatient.patient_visiting_hospital("12345678") == 9

def test_book_appointment():
    #assert book_appointment.book_appointment('9999999999', 12345678, 87654321, '17/10/2021', 'Cough', '08 00') == 20
    assert book_appointment.book_appointment('9999999999', 12345678, 87654321, '17-10-2020', 'Cough', '08 30') == 4
    assert book_appointment.book_appointment('9999999999', 12345678, 87654321, '17/13/2021', 'Cough', '09 00') == 7
    assert book_appointment.book_appointment('9999999999', 12345678, 87654321, '17/10/2020', 'Cough', '09 30') == 5
    assert book_appointment.book_appointment('9999999999', 12345678, 876543, '17/10/2022', 'Cough', '10 00') == 2
    assert book_appointment.book_appointment('9999999999', 123456, 87654321, '17/10/2022', 'Cough', '10 30') == 3
    assert book_appointment.book_appointment('999999999', 12345678, 87654321, '17/10/2022', 'Cough', '11 00') == 8
def test_check_date1():
    assert VaccineRegister.check_date("17/18/2000") == 4
    assert VaccineRegister.check_date("17/10/2022") == 3
    assert VaccineRegister.check_date("17-10-2000") == 1


def test_vaccine_booking():
    assert VaccineRegister.patient_details(123, 421, 'sri', 21, '23-06-2021', '8309886578', 'f') == 1
    assert VaccineRegister.patient_details(123, 421, 'sri', 21, '23/16/2021', '8309886578', 'f') == 4
    assert VaccineRegister.patient_details(123, 421, 'sri', 21, '23/06/2021', '8309886578', 'f') == 3

def test_check_date():
    assert book_appointment.check_date("17/10/2000") == 5
    assert book_appointment.check_date("17/10/2022") == 6
    assert book_appointment.check_date("17/13/2000") == 7
    assert book_appointment.check_date("17-10-2000") == 4


def test_check_mobile():
    # If mobile number 999999999 is present, following test works.
    # assert bookAppointment.check_mobile_no('9999999999') == 10
    assert book_appointment.check_mobile_no('501234999') == 8
    assert book_appointment.check_mobile_no('7501234999') == 10
    assert book_appointment.check_mobile_no('6501234999') == 9






def test_add_doctor():
    assert docregister.add_doctor(65412337, "riya", "cough", 12345678, "acd", 9632145808, 365412012369, "12345") == 1
    assert docregister.add_doctor(65412333, "vikas", "fever", 12345678, "acd", 9632145801, 365412012363, "12345") == 1
    assert docregister.add_doctor(65412334, "ajay", "cold", 12345678, "acd", 9632145802, 365412012364, "12345") == 1
    assert docregister.add_doctor(65412335, "swaroop", "detaist", 12345678, "acd", 9632145804, 365412012365,
                                  "12345") == 1
    assert docregister.add_doctor(65412336, "sai", "surgery", 12345678, "acd", 9632145805, 365412012366, "12345") == 1


def test_chech_id():
    assert docregister.id_check(65412337) == True
    assert docregister.id_check(65412333) == True
    assert docregister.id_check(65412334) == True
    assert docregister.id_check(65412335) == True
    assert docregister.id_check(65412336) == True
    assert docregister.id_check(65412131) == False
    assert docregister.id_check(65112332) == False
    assert docregister.id_check(65112333) == False
    assert docregister.id_check(65112334) == False
    assert docregister.id_check(65112337) == False



