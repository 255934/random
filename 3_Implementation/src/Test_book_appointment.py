import book_appointment


# doctors table should contain D_id = 1234567 H_id = 23456789.
def test_book_appointment():
    assert book_appointment.book_appointment('9999999999', 1234567, 23456789, '17/10/2021', 'Cough', '08 00') == 20
    assert book_appointment.book_appointment('9999999999', 1234567, 2345678, '17-10-2020', 'Cough', '08 30') == 4
    assert book_appointment.book_appointment('9999999999', 1234567, 2345678, '17/13/2020', 'Cough', '09 00') == 7
    assert book_appointment.book_appointment('9999999999', 1234567, 2345678, '17/10/2020', 'Cough', '09 30') == 5
    assert book_appointment.book_appointment('9999999999', 1234567, 234567, '17/10/2022', 'Cough', '10 00') == 2
    assert book_appointment.book_appointment('9999999999', 123456, 2345678, '17/10/2022', 'Cough', '10 30') == 3
    assert book_appointment.book_appointment('999999999', 23456789, 12345678, '17/10/2022', 'Cough', '11 00') == 9


def test_check_date():
    assert book_appointment.check_date("17/10/2000") == 5
    assert book_appointment.check_date("17/10/2022") == 6
    assert book_appointment.check_date("17/13/2000") == 7
    assert book_appointment.check_date("17-10-2000") == 4


def test_check_mobile():
    # If mobile number 999999999 is present, following test works.
    # assert bookAppointment.check_mobile_no('9999999999') == 10
    assert book_appointment.check_mobile_no('501234999') == 8
    assert book_appointment.check_mobile_no('7501234999') == 11
    assert book_appointment.check_mobile_no('6501234999') == 9
