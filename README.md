# User Registration System

This project is a simple user registration system made using Flask and MySQL.

The registration form takes the user's username, email, gender, and password.

For security, the password is hashed using bcrypt before it is stored in the MySQL database.

## Technologies Used

- Python
- Flask
- MySQL
- MySQL Connector
- bcrypt
- HTML
- CSS

## Project Structure

```text
project/
│
├── app.py
├── connect.py
├── requirements.txt
├── README.md
│
└── templates/
    └── register.html
````

 ## Database Setup

 First, create the database in MySQL.

```
CREATE DATABASE UserDB;

USE UserDB;
```

 Create the users table:

```
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

 The password column uses `VARCHAR(255)` because the bcrypt password hash is longer than a normal password.

 ## Install Required Packages

 Open the terminal in the project folder and run:

```
pip install -r requirements.txt
```

 The `requirements.txt` file contains:

```
Flask
mysql-connector-python
bcrypt
```

 ## MySQL Connection

 The MySQL connection is written in `connect.py`.

```
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="UserDB"
)
```

 Change the MySQL password if your MySQL server has a password.

 ## Running the Project

 Run the Flask application using:

```
python app.py
```

 After starting the application, open this address in the browser:

```
http://127.0.0.1:5000/
```

 ## Registration

 The registration form contains:

 - Username
- Email
- Gender
- Password

 The application checks that the required fields are filled in.

 The password must contain at least 6 characters.

 ## Password Hashing

 The password is not directly stored in the database.

 First, bcrypt creates a hash from the password:

```
password_hash = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)
```

 The hash is then converted to text:

```
password_hash = password_hash.decode("utf-8")
```

 Only the hashed password is stored in MySQL.

 For example, if the user enters:

```
password123
```

 the database will store something similar to:

```
$2b$12$............
```

 The original password is not stored in the database.

 ## Checking the Database

 After registering a user, open MySQL and run:

```
USE UserDB;

SELECT * FROM users;
```

 The result should show the registered user's information.

 The password column should contain a bcrypt hash instead of the original password.

 Example:

```
id    username    email              gender    password
1     testuser    test@gmail.com     Male      $2b$12$...
```

 ## Security Improvement

 Previously, the password was stored directly in the database.

 Now bcrypt is used to hash the password before saving it.

 This means that the original password is not stored as plain text in the database.

 ## Testing

 I tested the registration form by entering a username, email, gender, and password.

 After submitting the form:

 1. The form data is received by Flask.
2. The input is validated.
3. The password is hashed using bcrypt.
4. The user information is inserted into MySQL.
5. The registration success message is displayed.
6. The database was checked using `SELECT * FROM users;`.
7. The password was stored as a bcrypt hash.

 ## Result

 The registration system successfully stores user information in MySQL while protecting the user's password using bcrypt hashing.
