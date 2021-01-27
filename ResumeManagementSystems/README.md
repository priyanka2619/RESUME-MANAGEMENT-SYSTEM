# ResumeManagementSystems
Resume Management System will Maintain Multiple Employees Resumes.

# Menu Options
1) Home
2) Registration page
3) Login Page
4) View Profile
5) Update Profile
6) Delete Profile
7) Logout
8) About us

# Models
1) IndustriesModel
    a) Education
    b) IT
    c) Marketing
    
2) RegistrationModel
    a) Full Name
    b) Phone No (unique only)
    c) Username (Email)
    d) Password
    e) OTP
    e) Date (Auto date)
    
3) Login --- Registration
    a) username (Email)
    b) password 
    
4) Profile
    a) Name
    b) Higher Education
    c) Photo
    d) CV
    e) contact
    f) email
    g) Industries Type 

# Registration page
===== Required Fields =====
1) Name
2) Contact Number -- unique only
3) Photo
4) Email -- unique only
5) Password
---> If the user is registered send an OTP in a message and in a e-mail.
---> Allow the user to enter the OTP for 3 times, after 3rd attempt  block the user (with the same contact no and the same email id the user cannot register again)
---> If the user enter the proper OTP finish the user registration and send a confirmation Email and Text message as a OTP.


#Login page
=====Login with Required Fields=====
1) Email - email_id -- unique only
2) Password

Sessions -- After Login we cannot Register again & cannot Logout. 
After Login only we can see the Profile like View Profile, Update Profile & Delete Profile.

 #Resources
 Resume Management System is Consumer application as well as Provider application.
 
 To consume the service use given below api's:
 
 API:-
      
      Registration --> http://127.0.0.1:8000/api.registration_details/
      Profile      --> http://127.0.0.1:8000/api.profile_details/
            