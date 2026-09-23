# 🎓 University Management System

A Python-based **University Management System** built using **Streamlit** to manage colleges, students, and teachers through a simple and interactive web interface.

## 📌 Overview

The **University Management System** is a beginner-friendly application designed to demonstrate **Python Object-Oriented Programming (OOP)** concepts along with Streamlit application development.

The system allows users to:

* 🏫 Create and manage colleges
* 👨‍🎓 Add and manage student information
* 👨‍🏫 Add and manage teacher information
* 📋 Display students and teachers associated with a college
* 🏢 View all colleges created in the application

---

## 🚀 Features

### 🏫 College Management

* Create new colleges
* Store multiple college objects
* Select colleges while adding students or teachers
* View the list of available colleges

### 👨‍🎓 Student Management

Users can add students to a selected college with details such as:

* Student Name
* Roll Number
* Branch

The application also allows users to display the students belonging to a particular college.

### 👨‍🏫 Teacher Management

Users can add teachers to a selected college with details such as:

* Teacher Name
* Branch
* Subject

The application provides an option to display the teachers associated with a college.

### 📊 Interactive Dashboard

The application uses Streamlit to provide:

* Sidebar navigation
* Interactive forms
* Input fields
* Selection menus
* Dynamic display of records
* Session-based data management

---

## 🛠️ Tech Stack

| Technology     | Purpose                                   |
| -------------- | ----------------------------------------- |
| **Python**     | Application development                   |
| **Streamlit**  | Web application interface                 |
| **Python OOP** | Managing colleges, students, and teachers |

---

## 📂 Project Structure

```text
University-Management-System/
│
├── main.py
├── requirements.txt
└── README.md
```

### File Description

* `main.py` – Contains the main Python and Streamlit application logic.
* `requirements.txt` – Contains the required Python dependencies.
* `README.md` – Project documentation.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Akshara-Jadav/University-Management-System.git
```

### 2. Navigate to the Project Directory

```bash
cd University-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install Streamlit directly:

```bash
pip install streamlit
```

### 6. Run the Application

```bash
streamlit run main.py
```

The application will open in your browser using the local Streamlit URL displayed in the terminal.

---

## 🖥️ How to Use

After launching the application:

1. Open the **sidebar menu**.
2. Select **Create College**.
3. Enter the college name and create the college.
4. Select **Add Student** to add student information.
5. Select **Add Teacher** to add teacher information.
6. Use **Display Students** to view students.
7. Use **Display Teachers** to view teachers.
8. Use **List of Colleges** to view all created colleges.

---

## 🔄 Example Workflow

```text
Create College
      ↓
Add Students
      ↓
Add Teachers
      ↓
View Students
      ↓
View Teachers
      ↓
View Colleges
```

### Example

**College:** XYZ College

**Students:**

* Vyshnavi– CSE – Roll No: 101
* Dhiraj – ECE – Roll No: 102

**Teachers:**

* Dr. Achal – CSE – Python
* Prof. Raj – ECE – Digital Electronics

---

## 🧠 Concepts Used

This project demonstrates several important Python concepts:

* Object-Oriented Programming
* Classes and Objects
* Lists
* Functions
* Conditional Statements
* Loops
* User Input Handling
* Streamlit Session State
* Basic application navigation

---

## 💾 Data Storage

The application currently uses **Streamlit session state** to store data while the application is running.

> ⚠️ Data is temporary and is not stored permanently in a database. Data may be lost when the application session is restarted or refreshed depending on the session state.

---

## 🔮 Future Enhancements

The project can be further improved by adding:

* 🔐 User authentication and login
* 🗄️ Database integration using MySQL or SQLite
* ✏️ Edit and delete student/teacher records
* 🔍 Search and filter functionality
* 📊 University statistics and dashboards
* 📱 Improved responsive UI
* 📤 Export student and teacher records to CSV/Excel
* ☁️ Deployment using Streamlit Community Cloud

---

## 🎯 Learning Objective

The main objective of this project is to understand how **Python OOP concepts can be combined with Streamlit** to create a simple interactive application.

It also provides practical experience in organizing application logic, handling user inputs, managing objects, and building a basic web interface using Python.

---

## 👩‍💻 Author

**Akshara Jadav**

* GitHub: [Akshara-Jadav](https://github.com/Akshara-Jadav)

---

## 📄 License

This project is created for **educational and learning purposes**.

