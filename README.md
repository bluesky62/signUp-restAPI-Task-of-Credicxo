# signUp-restAPI-Task-of-Credicxo
Task:
Create REST APIs based on Django with PostgreSQL database. It 
should contain:
1. User Sign Up/Forgot Password APIs.
2. Uses JWT authentication.
3. Must define 3 user levels: 1. Super-admin, 2. Teacher, 3. Student (Use 
internal Django Groups to achieve the same).
4. Teacher must be able to add/list the students.
5. Admin must be able to add/list every user in the database.
6. Students must be able to see his information only.
7. Code should be commented for clarity.



Requests
Register the user
POST /users/register

{
    "username": "username",
    "email": "example@gmail.com",
    "password": "password"
}
Generate the access token
POST /api/token/

{
    "username": "username",
    "email": "example@gmail.com",
}
To reset password
POST /api/password_reset/

{
    "email": "example@gmail.com"
}
It'll print a token in Backend Terminal Console.
To confirm reset password
POST /api/password_reset/

{
    "token":"<token>",
    "password":"Password@123"
}
To add the new user to the database
POST /users/manage

{
    "username": "studentnew",
    "email": "studentnew@gmail.com",
    "password": "pass@123",
    "groups": [3]
}
Student (Group no 3) is unable to add anyone to the database.
Teacher (Group no 2) is able to add Students to the database.
Super-admin (Group no 1) is able to add anyone to the database.
To list users from the database
GET /users/manage

Student (Group no 3) is able to list his information from the database.

Teacher (Group no 2) is able to list Students' information from the database.

Super-admin (Group no 1) is able to list anyone's information from the database.




