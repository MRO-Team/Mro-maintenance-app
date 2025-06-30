# MRO Maintenance App

A simple web-based maintenance tracking system tailored for MRO (Maintenance, Repair, and Overhaul) operations.  
This app allows operators to report malfunctions, create maintenance requests, and lets managers update the status of ongoing tasks.

---

## 🚀 Features

- Operator panel for submitting malfunction reports
- Manager panel for updating request statuses
- Maintenance history tracking
- Simple and responsive user interface
- SQLite or Firebase for persistent data storage

---

## 🛠 Tech Stack

- *Frontend*: HTML, CSS, JavaScript  
- *Backend*: Python Flask  
- *Database*: SQLite (optionally Firebase)

---

## 📂 Project Structure

mro-maintenance-app/
│
├── backend/
│   ├── app.py
│   └── database.db
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── README.md
└── requirements.txt

---

## ▶ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mro-maintenance-app.git
cd mro-maintenance-app

2. Set Up the Backend

cd backend
pip install -r ../requirements.txt
python app.py

3. Launch the Frontend

Open frontend/index.html in your browser.
Make sure the Flask server is running at http://localhost:5000.

⸻

✅ TODO List
	•	Basic UI layout (HTML/CSS)
	•	Flask API endpoints for ticket creation and updates
	•	SQLite database setup
	•	Role-based UI (Operator vs Manager)
	•	Optional: Firebase backend integration

⸻

👤 Author

Serhad Hamamci , Öykü Koç
Developer & Project Owner
GitHub: @hamamciserhad , @oykukoc

⸻

This project is part of an internship portfolio and aims to demonstrate full-stack development skills with real-world industrial relevance.
