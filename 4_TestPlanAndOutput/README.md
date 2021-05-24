# Test Plan

## High Level Test Plan

| Test ID | Description | Exp I/P | Exp O/P |	Actual Output | Type of Test |
| --- | --- | --- | --- | --- | --- |
| H_P1 | Check if the new patient is able to register | Details of the user: Name, Aadhar No., Card details | SUCCESS | TBD | Requirement Based |
| H_P2 | Check if the patient is able to login | Aadhar No., Password | SUCCESS | TBD | Requirement Based |
| H_P3 | Check if the patient is able to book a vaccine | Hospital, Doctor, Date | SUCCESS | TBD | Requirement Based |
| H_P4 | Check if the patient is able to book an appointment | Hospital, Doctor, Date | SUCCESS | TBD | Requirement Based |
| H_P5 | Check if the patient is able to make payment | Card details | Balance amount | TBD | Requirement Based |
| H_A1 | Check if the admin is able to login | Admin credentials | SUCCESS | TBD | Requirement Based |
| H_A2 | Check if the admin is able to add new hospital details | Hospital name, Address | SUCCESS | TBD | Requirement Based |
| H_A3 | Check if the admin is able to add new doctor details | Doctor name, Specialization, Experience | SUCCESS | TBD | Requirement Based |
| H_A4 | Check if the admin is able to edit hospital details | Hospital ID, Name, Address | SUCCESS | TBD | Requirement Based |
| H_A5 | Check if the admin is able to edit a doctor's details | Doctor ID, Name, Specialization, Experience | SUCCESS| TBD | Requirement Based |
| H_A6 | Check if the admin is able to delete hospital details | Hospital ID | SUCCESS | TBD | Requirement Based |
| H_A7 | Check if the admin is able to delete doctor's details | Doctor ID | SUCCESS | TBD | Requirement Based |
| H_D1 | Check if the doctor is able to login | Doctor's credentials | SUCCESS | TBD | Requirement Based |
| H_D2 | Check if the doctor is able to view all his appointment details | Choose appropriate option | SUCCESS | TBD | Requirement Based |
| H_D3 | Check if the doctor is able to view his patients details | Choose appropriate option | SUCCESS | TBD | Requirement Based |


## Low Level Test Plan 

| Test ID | Description | Exp I/P | Exp O/P |	Actual Output | Type of Test |
| --- | --- | --- | --- | --- | --- |
| L_01 | Check if the Aadhar number is 12-digit | Aadhar number | SUCCESS | TBD | Technical Based |
| L_02 | Check if the card number is 16-digit | Card number | SUCCESS | TBD | Technical Based |
| L_03 | Check if length of the password is within the limits | Password | SUCCESS | TBD | Boundary Based |
| L_04 | Check if the user's balance is within the limits | Balance | SUCCESS | TBD | Boundary Based |
| L_05 | Check if the user credentials are present in the database | Login credentials | pass | TBD | Technical Based |
| L_06 | Check if the user enters valid Hospital ID during vaccine registration | Hospital ID | pass | TBD | Technical Based |
| L_07 | Display error message if no slots available for vaccination | Hospital ID | pass | TBD | Technical Based |
| L_08 | Check if the user enters valid Hospital ID for appointment | Hospital ID | pass | TBD | Technical Based |
| L_09 | Check if the user enters valid Doctor ID for appointment | Doctor ID | pass | TBD | Technical Based |
| L_10 | Check if the user's payment details match the database |Card number and security pin | pass | TBD | Technical Based |
| L_11 | Check if the user has enough balance to make the payment | Card number and security pin | pass | TBD | Technical Based |
| L_12 | Check if the user's balance is within the limits to credit money | Credit amount | SUCCESS | TBD | Boundary Based |
