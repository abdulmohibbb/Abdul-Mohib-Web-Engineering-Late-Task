# Student Course Registration System Report

## Architecture
This project uses a Django MVC-style architecture with server-rendered HTML templates, Django forms, ORM models, and SQLite as the default database. The `registration` app contains the core business logic for student registration, login, course enrollment, and course dropping. Templates render the user interface, while Django views coordinate form validation, authentication, and database transactions.

## Technologies Used
- Backend: Django
- Frontend: HTML, CSS, JavaScript-ready structure with responsive server-rendered templates
- Database: SQLite (Django default)
- Authentication: Django built-in authentication system
- Validation: Django form validation and model constraints, plus client-friendly HTML form controls

## Security Measures
- Passwords are stored using Django’s built-in password hashing system.
- CSRF protection is enabled for all form submissions.
- Login-protected pages use `@login_required` so only authenticated users can enroll or drop courses.
- Server-side validation checks duplicate email addresses, duplicate student IDs, and duplicate enrollments.
- Database-level uniqueness constraints prevent duplicate student profiles and duplicate enrollments even if requests race.
- POST-only actions are enforced for enrollment and drop actions to reduce accidental state changes.

## Functional Summary
Students can register, log in, view their dashboard, browse available courses, enroll in courses, and drop enrolled courses. The interface is responsive and adapts to mobile and desktop screens through flexible layouts and media queries.
