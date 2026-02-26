# 📝 Online Exam Management System

A Web-Based Online Exam Management System built using Python (Flask) and SQLite.  
This project allows students to register, login, attend exams, and view their results automatically.

---    

## 🚀 Features

- 👤 Student Registration
- 🔐 Secure Login System
- 📝 Online Multiple Choice Exam
- 📊 Automatic Score Calculation
- 💾 Result Storage in Database
- 🚪 Logout System
- 🎨 Clean UI with CSS

---

## 🛠 Technologies Used

- Python 3
- Flask Framework
- SQLite Database
- HTML5
- CSS3
- Jinja2 Template Engine
- Git & GitHub

---

## 📂 Project Structure

Online-Exam-Management-System/
│
├── app.py
├── exam.db
├── README.md
│
├── static/
│ └── style.css
│
└── templates/
├── register.html
├── login.html
├── exam.html
└── result.html

---

## ⚙ How to Run the Project

### 1️⃣ Clone the Repository


### 2️⃣ Navigate to Project Folder


cd Online-Exam-Management-System


### 3️⃣ Install Flask


pip install flask


### 4️⃣ Run the Application


python app.py


### 5️⃣ Open in Browser


http://127.0.0.1:5000/


---

## 🗄 Database Details

Database Name: `exam.db`

The system automatically creates 3 tables:

### 👤 students
- id (Primary Key)
- name
- email
- password

### ❓ questions
- id
- question
- option1
- option2
- option3
- option4
- answer

### 📊 results
- id
- student_id
- score

---

## 🔄 Application Flow

1. Student registers
2. Student logs in
3. Questions are loaded dynamically from database
4. Student submits exam
5. Score is calculated automatically
6. Result is stored in database
7. Result page is displayed

---

## 🔐 Security Features

- Session-based Authentication
- Parameterized SQL Queries (Prevents SQL Injection)
- Login Validation

---

## 🎯 Future Improvements

- Admin Panel
- Exam Timer
- Random Question Generator
- Result History Page
- Pass/Fail Status
- Password Hashing

---

## 👨‍💻 Author

**Arun Kumaran**  
GitHub: https://github.com/arunkumaransiva  

---

## 📌 Project Type

Mini Project (Academic Purpose)  
Built for learning Flask Web Development.

