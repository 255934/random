# Introduction

Patient management system helps the users to register for vaccine and  book an appointment with a particular doctor at a particular hospital. It also has an availability to pay their hospital bills through this platform and also provides some ways to pay them. This platform also has an option to register for health insurance. The hospitals and doctors can register through the admin portal and these hospitals and doctors are made available to the users to get an appointment and register for the vaccine.

# Research

Advancement of health and medical industry is much more important than any others and taking the current situation into consideration we have came up with an idea to improvise the traditional way of taking appiontments with digitalising them. The digitilised mode of consulting the doctors helps the users to save time and effort which they do in a traditional format and regarding the vaccine the user has a clear view of availability of vaccine at particular hospital and if available the user can directly register to avail it.

## Advantages
* Saves  time
* Saves effort
* Easy access
* 24/7 availability


# 4W&#39;s and 1&#39;H

## Who:
- Product owner : Company Overseeing Hospitals
- Organization: L&T Technology Services
- Developers:  @udaykiran640 @99004491-Milan @HanumanthaReddy-99004496 @Vinuthna-99004497 @Gowri-sri-priya
- Tester: @udaykiran640 @99004491-Milan @HanumanthaReddy-99004496 @Vinuthna-99004497 @Gowri-sri-priya
- Lead / Manager / Architects:  @Gowri-sri-priya (scrum leader)

## What:
  Patient management system is to facilitate organization that handles a chain of hospitals.By maintaining the records of Hospitals that are associated, doctors working in them and the records of patient visiting them. If records are maintained on paper there is a chnace of it getting lost, so our aim is to digitize that process. Client will also be able veiw all the records, search a patients detail, delete a record. General Users visiting the app can book appointment with a doctor or register for vaccine


## When:
The deadline is 25th of may and the project was started on 17th of april. The duration of the project is of 1 weeks roughly.

## Where:

Application will be running on desktops of Client organization and General user that visit the application.

## How:
The application is written in Python and no extra dependencies are required on the clients system.

## SWOT analysis
![swot](https://github.com/GENESIS2021Q1/sdlc-team-41/blob/main/1_Requirements/SWOT.png)

# Requirements

## High Level Requirements: 
| ID | Description | Category | Status | 
| ----- | ----- | ------- | ---------|
| HR01| Login/Registeration | Techincal | TBD-S1 |
| HR02 | Digitizing Patient Record| Techincal | TBD-S1 | 
| HR03 | Vaccine Registration | Techincal | TBD-S1 |
| HR04| Digitizing Hosptial Record | Techincal | TBD-S1 |
| HR05| Digitizing Doctor Record | Techincal | TBD-S1 |
| HR06|Payments| Techincal | TBD-S1 |

##  Low level Requirements:
 
| ID | Description | HLR ID | Status (Implemented/Future) |
| ------ | --------- | ------ | ----- |
| LR01 |Providing a login system which will give access to only authorised personal(admin) to perform certain features| HR01 | TBD-S1 |
| LR01.1 | Registeration for new user/ Login for user to perform actions like Book appointment, Book Vaccine Slot, Payments | HR01 | TBD-S1 |
| LR02 | Book an appointment (user) | HR01 | TBD-S1 |
| LR02.1 | Display all appointment (admin)| HR01 | TBD-S1 |
| LR02.2| Update appointment, using adharcard number (user if his own through which he logged in/admin can do anyone) | HR01 | TBD-S1 |
| LR02.3 |Search appointment using adharcard number (user if his own through which he logged in/admin can do anyone)| HR01 | TBD-S1 |
| LR02.4 |Delete appointment from the file (user if his own through which he logged in/admin can do anyone) | HR01 | TBD-S1 |
| LR03| Book an vaccine appointment (user) | HR01 | TBD-S1 |
| LR03.1 | Display all vaccine appointment (admin)| HR01 | TBD-S1 |
| LR03.2| Update vaccine appointment, using adharcard number (user if his own through which he logged in/admin can do anyone) | HR01 | TBD-S1 |
| LR03.3 |Search vaccine appointment using adharcard number (user if his own through which he logged in/admin can do anyone)| HR01 | TBD-S1 |
| LR03.4 |Delete vaccine appointment from the file (user if his own through which he logged in/admin can do anyone) | HR01 | TBD-S1 |
| LR03.5 |The hospital capacity of vacinating people per day should be pre feed| HR02 | TBD-S1 |
| LR04|Add hospital details (admin) | HR01 | TBD-S1 |
| LR04.1 | Display all hospitals (admin)| HR01 | TBD-S1 |
| LR04.2| Update hospital details (admin) | HR01 | TBD-S1 |
| LR04.3 |Search hospital details (admin)| HR01 | TBD-S1 |
| LR04.4 |Delete hospital details (admin) | HR01 | TBD-S1 |
| LR05|Add doctor details (admin) | HR01 | TBD-S1 |
| LR05.1 | Display all doctor (admin)| HR01 | TBD-S1 |
| LR05.2| Update doctor details (admin) | HR01 | TBD-S1 |
| LR05.3 |Search doctor details (admin)| HR01 | TBD-S1 |
| LR05.4 |Delete doctor details (admin) | HR01 | TBD-S1 |
| LR06|Pay using wallet | HR01 | TBD-S1 |
| LR06.1|Add money | HR01 | TBD-S1 |
| LR06.2|Add money through UPI | HR01 | TBD-S1 |
| LR06.3|Registered UPI user | HR01 | TBD-S1 |
| LR06.4|New UPI user | HR01 | TBD-S1 |
| LR06.5|Medical Insurance (Future Scope) | HR01 | TBD-S1|



