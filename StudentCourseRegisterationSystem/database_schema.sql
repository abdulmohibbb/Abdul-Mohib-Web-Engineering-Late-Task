CREATE TABLE registration_studentprofile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED,
    student_id VARCHAR(30) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL DEFAULT '',
    major VARCHAR(100) NOT NULL DEFAULT '',
    created_at DATETIME NOT NULL
);

CREATE TABLE registration_course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(20) NOT NULL UNIQUE,
    title VARCHAR(150) NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    credits SMALLINT UNSIGNED NOT NULL CHECK (credits >= 1),
    capacity SMALLINT UNSIGNED NOT NULL CHECK (capacity >= 1),
    created_at DATETIME NOT NULL
);

CREATE TABLE registration_enrollment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES registration_studentprofile(id) DEFERRABLE INITIALLY DEFERRED,
    course_id INTEGER NOT NULL REFERENCES registration_course(id) DEFERRABLE INITIALLY DEFERRED,
    enrolled_at DATETIME NOT NULL,
    UNIQUE(student_id, course_id)
);
