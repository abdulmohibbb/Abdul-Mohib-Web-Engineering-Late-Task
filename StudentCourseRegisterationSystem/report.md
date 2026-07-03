# Student Course Registration System Report

## 1. Project Overview
The Student Course Registration System is a Django-based web application for managing student accounts and course enrollment. It supports user registration, login, dashboard access, browsing courses, enrolling in a course, and dropping a course. The project is intentionally built with a server-rendered HTML interface so it is easy to understand, deploy, and mark in a classroom environment.

The application uses SQLite, Django’s default database engine, so it runs locally with no external database server. The frontend is built with plain HTML, CSS, and a small amount of JavaScript. The backend is written in Django and uses Django’s built-in authentication, form handling, ORM, and CSRF protection.

## 2. Features Implemented
The system includes the following features:

- Student registration with username, name, email, student ID, phone, major, and password confirmation.
- Student login and logout.
- Student dashboard showing profile details, total enrollments, active courses, and available courses.
- Course catalog page with course code, title, description, credits, capacity, enrolled count, and seats left.
- Course enrollment with duplicate-enrollment prevention.
- Course drop functionality for courses already enrolled by the logged-in student.
- Sample seed courses added automatically through a Django data migration.
- Responsive layout for mobile and desktop screens.
- Server-side and client-friendly validation.
- Admin support for managing students, courses, and enrollments.

## 3. Technologies Used
### Backend
- Django 6.x
- Django ORM
- Django authentication system
- Django forms and validation

### Frontend
- HTML5
- CSS3 with responsive layouts and media queries
- JavaScript for confirmation before dropping a course

### Database
- SQLite
- Django migrations for schema creation and sample data

### Other Tools
- Google Fonts for typography in the interface

## 4. Architecture
The application follows Django’s standard MVT architecture:

- Model: database tables and business entities such as students, courses, and enrollments.
- View: Django view functions that handle registration, login flow, dashboard rendering, enrollment, and drop actions.
- Template: server-rendered HTML pages for the public and authenticated user interface.

The core app is the `registration` app. It contains the main models, forms, views, URL routes, admin configuration, migrations, templates, and static assets. The project-level Django package configures settings, root URLs, database connection, and template discovery.

## 5. Project Structure
Main files and folders in the submission:

- `manage.py` - Django command-line entry point.
- `StudentCourseRegisterationSystem/settings.py` - project settings, installed apps, database, templates, and login redirects.
- `StudentCourseRegisterationSystem/urls.py` - root URL routing.
- `registration/models.py` - database models for student profiles, courses, and enrollments.
- `registration/forms.py` - registration and login forms with validation.
- `registration/views.py` - all request handling and business logic.
- `registration/urls.py` - app-level routes.
- `registration/admin.py` - Django admin registration for models.
- `registration/templates/` - HTML pages.
- `registration/static/registration/styles.css` - responsive styling.
- `registration/static/registration/app.js` - small client-side confirmation script.
- `registration/migrations/` - database schema migrations and course seed data.
- `database_schema.sql` - SQL version of the schema for submission.
- `report.md` - this report.

## 6. Database Design
The database contains three custom tables:

- `StudentProfile` - stores the profile linked to a Django user account.
- `Course` - stores course details such as code, title, description, credits, and capacity.
- `Enrollment` - stores the many-to-many relationship between students and courses.

### Relationships
- Each student profile belongs to exactly one Django user account.
- A student can enroll in many courses.
- A course can have many students.
- The `Enrollment` table prevents duplicate registrations using a uniqueness constraint on the student-course pair.

### Important Constraints
- `student_id` is unique.
- `course.code` is unique.
- A student cannot enroll in the same course twice.
- Credits and capacity must be at least 1.

The SQL version of the schema is included in `database_schema.sql` for easy review.

## 7. Validation and Business Rules
Validation is implemented on both the frontend-friendly form layer and the server side.

### Registration Validation
- Username, password, and password confirmation are validated through Django’s built-in user creation form.
- Email addresses must be unique.
- Student IDs must be unique.
- Optional fields such as phone and major are allowed to remain blank.

### Course Enrollment Validation
- The student must be logged in.
- The course must exist.
- The student cannot enroll in a course twice.
- Enrollment is blocked if the course is full.
- Enrollment happens inside a database transaction to reduce race-condition issues.

### Course Drop Validation
- The student must be logged in.
- The student can only drop enrollments that belong to their own account.
- The action is POST-only.

## 8. Security Measures
The project includes the following security-related protections:

- Django hashes passwords automatically before storing them.
- CSRF protection is enabled for all forms.
- Login-required access control protects dashboard, enrollment, and drop pages.
- POST-only actions are used for enrollment and dropping courses.
- Database uniqueness constraints help protect data integrity.
- The drop action is confirmed in the browser using JavaScript to reduce accidental submissions.

## 9. Responsive UI and UX
The interface is designed to work on mobile and desktop screens.

### Visual Design
- Dark, layered background with gradient accents.
- Card-based layout for readability.
- Clear call-to-action buttons.
- Consistent spacing and rounded components.

### Responsiveness
- Flexible grid layouts adapt between desktop and mobile.
- The course cards, stats, and forms stack vertically on narrow screens.
- Buttons expand to full width on small screens for easier tapping.

## 10. How the Application Works
### Registration Flow
1. A new user opens the registration page.
2. The user enters account and student details.
3. Django validates the form on the server.
4. A Django `User` record and a linked `StudentProfile` record are created.
5. The user is automatically logged in and redirected to the dashboard.

### Login Flow
1. The user enters username and password.
2. Django authenticates the credentials.
3. The user is redirected to the dashboard after successful login.

### Enrollment Flow
1. The student opens the course page.
2. Available course data is loaded from SQLite.
3. The student clicks enroll on a selected course.
4. The server checks duplicates and capacity.
5. If valid, an `Enrollment` row is inserted.

### Drop Flow
1. The student clicks drop on an enrolled course.
2. A confirmation prompt appears in the browser.
3. The server verifies ownership of the enrollment.
4. The enrollment row is deleted.

## 11. Setup Instructions
Follow these steps to run the project from a fresh clone.

### 11.1 Clone the Repository
```bash
git clone <your-repository-url>
cd "Web Engineering Late Task"
```

### 11.2 Enter the Django Project Folder
```bash
cd StudentCourseRegisterationSystem
```

### 11.3 Create a Virtual Environment
Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 11.4 Install Requirements
```bash
pip install -r requirements.txt
```

If you prefer manual installation, the project only needs Django:
```bash
pip install Django==6.0.6
```

### 11.5 Apply Database Migrations
```bash
python manage.py migrate
```

This creates the SQLite database schema and seeds the sample courses.

### 11.6 Create an Admin User Optional
```bash
python manage.py createsuperuser
```

Use this only if you want to manage courses, students, or enrollments from the Django admin panel.

### 11.7 Run the Development Server
```bash
python manage.py runserver
```

Open the browser at `http://127.0.0.1:8000/`.

## 12. Testing and Verification
The project was validated by running Django system checks and applying migrations successfully. The following behaviors are included in the implementation:

- Project loads without Django configuration errors.
- Database schema builds successfully on SQLite.
- Sample courses are inserted through a migration.
- Authentication, enrollment, and drop routes are wired through the project URL configuration.

## 13. What Is Included in the Submission
The submission contains:

- Complete Django source code.
- SQLite-based database schema.
- SQL schema export file.
- A detailed report.
- Responsive HTML templates.
- CSS and JavaScript assets.

## 14. Conclusion
This project delivers a complete student course registration workflow using Django and SQLite. It satisfies the required functionality for user registration, login, enrollment, and course dropping, while also providing server-side validation, responsive design, and a clear project structure that is easy to run and evaluate.
