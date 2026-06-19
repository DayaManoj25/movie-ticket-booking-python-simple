# 🎬 Movie Ticket Booking System

A Python-based console application for managing movie ticket reservations and customer bookings. The system allows users to select movies, choose show timings, reserve seats, calculate ticket prices, order snacks, and store booking information in a MySQL database.

> 🌟 This was my first programming project, developed during my Higher Secondary (12th Grade) Computer Science studies. It introduced me to Python programming, database management, and software development fundamentals.

---

## 📌 About The Project

Movie Ticket Booking System simulates the booking workflow of a multiplex cinema. Users can browse available movies, select preferred show timings, choose seats, purchase tickets, and save booking details to a database.

The project was built to demonstrate the practical use of Python with MySQL while solving a real-world problem through programming.

---

## 🚀 Features

- Browse available movies and ratings
- Select movie show timings
- Reserve multiple seats
- Prevent duplicate seat selection
- Support for Adult, Child, and Senior Citizen tickets
- Automatic ticket price calculation
- Optional snack ordering
- Customer information management
- Booking summary generation
- MySQL database integration
- Error handling and input validation

---

## 🛠 Tech Stack

- **Language:** Python
- **Database:** MySQL
- **Connector:** mysql-connector-python
- **Environment:** Command Line Interface (CLI)

---

## 🗄 Database Integration

The application stores booking details in a MySQL database including:

- Movie Information
- Show Date and Time
- Selected Seats
- Customer Details
- Ticket Type
- Number of Tickets
- Total Amount
- Snack Orders

---

## 📂 Project Structure

```text
Movie-Ticket-Booking-System/
│
├── python.py
├── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/DayaManoj25/Movie-Ticket-Booking-System.git
```

### Install Required Package

```bash
pip install mysql-connector-python
```

### Configure MySQL Connection

Update the following credentials inside the Python file:

```python
conn = sql.connect(
    host='localhost',
    user='root',
    passwd='YOUR_PASSWORD'
)
```

---

## ▶️ Running The Project

```bash
python python.py
```

---

## 🎟 Booking Process

1. Select a movie using Movie ID.
2. Choose a preferred show date.
3. Select an available show timing.
4. Reserve seats.
5. Enter customer information.
6. Choose ticket category.
7. Order snacks (optional).
8. Review booking details.
9. Save booking information to MySQL.

---

## 📚 What I Learned

Through this project, I gained practical experience in:

- Python Programming
- SQL Queries
- MySQL Database Connectivity
- Input Validation
- Data Management
- Exception Handling
- Real-World Problem Solving

This project became the foundation for my later work in software development, AI, and full-stack applications.

---

## 🔮 Future Improvements

- GUI using Tkinter
- Online Payment Integration
- User Authentication
- Ticket Cancellation System
- Real-Time Seat Availability
- Email Ticket Confirmation
- QR Code Based Tickets
- Web Version using Flask/Django

---

## 👨‍💻 Author

**Daya Manoj**

First Programming Project • Higher Secondary Computer Science Project

Built using Python and MySQL as an introduction to software development and database-driven applications.

---

## ⭐ A Small Milestone

Every developer has a project where everything starts.

For me, this Movie Ticket Booking System was that project.
It was my first step into programming and eventually led me toward building AI applications, web platforms, and machine learning projects.
