# 🩸 Blood Management System

A full-stack web application built using **Flask**, **MySQL**, and **Bootstrap** that streamlines the process of **donor registration**, **blood request management**, **inventory tracking**, and **hospital/blood bank administration**.  
Created as a college project to strengthen backend and full-stack development skills.
---

## 🛠 Tech Stack

| Category       | Tools Used                            |
|----------------|----------------------------------------|
| Frontend       | HTML, CSS, JavaScript, Bootstrap       |
| Backend        | Python Flask, REST API                 |
| Database       | MySQL (Relational DB)                  |
| Version Control| Git, GitHub                            |
| Others         | Flask-CORS, JSON, Form Handling        |

---

## 🚀 Features

### 👨‍⚕️ Donor Module
- Register donors with details like name, age, contact, blood type, and donation date
- View donor list (via admin panel)

### 🧍‍♂️ Recipient Module
- Request blood by entering required blood group and contact info
- Admin can update request status (Pending, Completed, Rejected)

### 🏥 Hospital Module
- Register hospitals with name, location, staff, and contact
- View all registered hospitals

### 🏦 Blood Bank Module
- Add blood banks and manage them via admin panel
- Manage inventory by bank ID and blood type

### 📦 Blood Inventory Module
- Add or update blood stock
- Track quantity and expiry date of each blood unit

### 🔐 Admin Panel
- Protected via password (`admin123`) for safety
- Manage/view donors, recipients, hospitals, blood banks, and inventory

---

## 🖼 UI Screenshots
<!-- Replace with your actual images -->
- 🏠 Home Page  
- 📝 Donor Registration Form  
- 🏥 Hospital Registration  
- 📋 Admin Panel with Record Viewing  

---

## 📂 Project Structure

```bash
BloodManagementSystem/
├── app.py               # Flask backend (API logic)
├── blooddb.sql          # MySQL schema creation
├── index.html           # Main frontend page
├── style.css            # Custom styling
├── script.js            # Frontend logic and API calls
├── README.md            # Project documentation

## 🧑‍💼 About the Author

**Keshav Suresh Bansal** is a Computer Science undergraduate with a passion for backend development, AI/ML, and full-stack projects.  
This project was created as a part of his journey to deepen understanding of APIs, databases, and web integration.

- 🔭 Currently working on Data Science and AIML projects
- 📫 Reach out: [LinkedIn](https://linkedin.com/in/keshav-suresh-bansal-254412359) | [GitHub](https://github.com/KeshavSB)
- 💡 Motto: *"Learn by building."*
