# 🎓 Educational Course Management System (Django)

An educational web platform built using **Django** and **Django REST Framework** that helps students easily browse courses and watch lecture chapters through a structured academic hierarchy.
The project exposes **~50 API endpoints**, making it suitable for any developer who wants to build a custom frontend (Web / Mobile) on top of it.
The backend was developed first as a standalone API, then later extended into a full-stack application.


---

## 📌 Project Description

This project provides a simple and organized way for students to access their academic content using the following hierarchy:

**College → Section → Stage → Subject → Chapter**

Students can browse courses without logging in, while logged-in users can track their viewing history.

The system is backend-focused with a clean and responsive frontend built using HTML, CSS, and JavaScript.

---

## 🚀 Features

### ✅ Course Browsing (No Login Required)
- Browse colleges, sections, stages, subjects, and chapters freely.
- Easy navigation through dependent selections.

### ✅ Dynamic Dependent Dropdowns
- Selecting a college loads related sections.
- Selecting a section loads related stages.
- Selecting a stage loads related subjects.
- Implemented using JavaScript and REST APIs.

### ✅ Chapters & Lectures
- Each chapter includes:
  - Chapter title
  - Description
  - YouTube lecture link

### ✅ User Authentication (Optional)
- Login is required only to:
  - Save watch history
  - Track viewed chapters
- Browsing content does not require login.

### ✅ Responsive Design
- Fully responsive layout.
- Works on mobile, tablet, and desktop devices.
- Centered and user-friendly interface.

---

## 🛠️ Technologies Used

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Database:** SQLite / MySQL
- **Authentication:** Django Authentication / dj-rest-auth
- **API Documentation:** Swagger (optional)
- **Version Control:** Git & GitHub

---

## 🗂️ Project Structure

project_root/
│
├── config/                     # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── courses/                    # Main application
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── api_urls.py             # API routes
│   ├── api_views.py            # API views (DRF)
│   ├── views.py                # Frontend views
│   ├── front_urls.py           # Frontend URLs
│   ├── models.py               # College, Section, Stage, Subject, Chapter
│   ├── forms.py
│   ├── apps.py
│   └── tests.py
│
├── templates/                  # HTML templates
│   ├── select_course.html
│   ├── chapters.html
│   ├── login.html
│   ├── register.html
│   └── full_watch_history.html
│
├── .env                        # Environment variables
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt

The project follows a clear separation between API logic and frontend views, allowing the backend to be reused independently.
---

## 🧩 Data Models (Simplified)

- **College**
- **Section** (related to College)
- **Stage** (related to Section)
- **Subject** (related to Stage)
- **Chapter** (related to Subject)
- **WatchHistory** (related to User & Chapter)

---

