# Basketball Position Quiz

This is a personality quiz to tell you your preferred basketball position based on your answers. 

In this quiz, you will:

1. Enter your metrics (ie. height, weight, years of experience)
2. Answer the quiz questions
3. Find out the results and repeat if you want!
4. If you have a admin login, you'll be able to log into the account and access inputted information. 

Possible results:
  - Guard
  - Forward
  - Center
  - Guard or Forward
  - Forward or Center
  - Guard or Center

In-Program Classes:

1. Person
  - This class is the parent class of the User and Admin classes. The Person class will read and write the user_info csv and will read the admins csv

2. Admin
  - This class will allow for admins to login and view or remove user infomation, if there's valid login information. This is also the parent class for the User class

3. User
  - This class inherits both the Person and Admin classes and will gather the user's information and ask different questions to determine the result
