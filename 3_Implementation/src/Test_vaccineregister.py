import VaccineRegister


def test_check_date():
    assert VaccineRegister.check_date("17/18/2000") == 4
    assert VaccineRegister.check_date("17/10/2022") == 3
    assert VaccineRegister.check_date("17-10-2000") == 1


def test_vaccine_booking():
    assert VaccineRegister.patient_details(123, 421, 'sri', 21, '23-06-2021', 8309886578, 'f') == 1
    assert VaccineRegister.patient_details(123, 421, 'sri', 21, '23/16/2021', 8309886578, 'f') == 4
    assert VaccineRegister.patient_details(123, 421, 'sri', 21, '23/06/2021', 8309886578, 'f') == 3
