# 🧑‍💼 Employee Management System (Python + MySQL)

This is a simple **Employee Management System** built using **Python (Flask)**, **MySQL**, **HTML**, and **CSS**.

## 🚀 Features

- Add new employees
- Edit employee details
- Delete employees
- View employee list in table format
- Responsive frontend with clean UI

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS
- **Database:** MySQL

## 🗃️ Database Structure

### Table: `employees`

| Column   | Type         |
|----------|--------------|
| id       | INT, Primary Key, Auto Increment |
| name     | VARCHAR(100) |
| phone    | VARCHAR(15)  |
| salary   | FLOAT        |

## 📂 Folder Structure

project/ 
    ├── app.py 
    ├── templates/ 
        │ └── index.html
    ├── static/ 
          │ └── style.css 
      └── README.md


  ## ▶️ How to Run

1. Install requirements:
    
    pip install flask mysql-connector-python
    

2. Setup MySQL database and table:
    
    CREATE DATABASE employee_db;

    USE employee_db;

    CREATE TABLE employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(15),
        salary FLOAT
    );
    

3. Run the app:
    python app.py

4. Open in browser:
    http://localhost:5000
