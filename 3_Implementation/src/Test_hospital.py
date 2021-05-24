from HospitalDetailsAdd import hospital_add
from DeleteHospital import hospital_delete
from HospitalDisplayPatient import patient_visiting_hospital


def test_add():
    assert hospital_add("1234567", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 0
    assert hospital_add("123456789", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 7
    assert hospital_add("1234567a", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 1
    assert hospital_add("12345678", "BK", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 2
    assert hospital_add("12345678", "dasdssadasdsdasdassdsa", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 3
    assert hospital_add("12345678", "BKMS1", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 4

    assert hospital_add("12345678", "BKMS", "1999-11-19", "100a", "9004088473", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 6
    assert hospital_add("12345678", "BKMS", "1999-11-19", "100", "900408847", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 8
    assert hospital_add("12345678", "BKMS", "1999-11-19", "100", "90040884732", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 9
    assert hospital_add("12345678", "BKMS", "1999-11-19", "100", "900408847a", "BKMS@gmail.com",
                        "dasdssadasdsdasdassdsa") == 10
    assert hospital_add("12345678", "BKMS", "1999-11-19", "100", "9004088473", "BKMSgmail.com",
                        "dasdssadasdsdasdassdsa") == 11
    assert hospital_add("12345678", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdss") == 12
    assert hospital_add("12345678", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssdsasdasdsa") == 100
    assert hospital_add("12345668", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssdsasdasdsa") == 100
    assert hospital_add("12345668", "BKMS", "1999-11-19", "100", "9004088473", "BKMS@gmail.com",
                        "dasdssdsasdasdsa") == 13


def test_delete():

    assert hospital_delete("1234567") == 0
    assert hospital_delete("123456789") == 7
    assert hospital_delete("1234567a") == 1
    assert hospital_delete("67350000") == 13
    assert hospital_delete("12345668") == 100


def test_display_patient():
    assert patient_visiting_hospital("1234567") == 0
    assert patient_visiting_hospital("123456789") == 7
    assert patient_visiting_hospital("1234567a") == 1
    # vinuthna will have to make sure that no entry in appointment with h_id==00000
    assert patient_visiting_hospital("00000") == 8
    # vinuthna will have to make sure that there is atleast 1 entry in appointment with h_id==12345678
    assert patient_visiting_hospital("12345678") == 9
