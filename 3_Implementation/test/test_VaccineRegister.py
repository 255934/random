import vaccine_booking


def test_check_date():
    assert vaccine_booking.check_date("17/18/2000") == 4
    assert vaccine_booking.check_date("17/10/2022") == 3
    assert vaccine_booking.check_date("17-10-2000") == 1


def test_vaccine_booking():
    assert vaccine_booking.patient_details(123, 421, 'sri', 21, '23-06-2021', 8309886578, 'f') == 1
    assert vaccine_booking.patient_details(123, 421, 'sri', 21, '23/16/2021', 8309886578, 'f') == 4
    assert vaccine_booking.patient_details(123, 421, 'sri', 21, '23/06/2021', 8309886578, 'f') == 3