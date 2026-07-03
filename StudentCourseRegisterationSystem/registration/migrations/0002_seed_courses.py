from django.db import migrations


COURSES = [
    {
        'code': 'CSE101',
        'title': 'Introduction to Programming',
        'description': 'Fundamentals of programming, problem solving, and Python basics.',
        'credits': 3,
        'capacity': 30,
    },
    {
        'code': 'CSE201',
        'title': 'Database Systems',
        'description': 'Relational design, SQL, normalization, and transaction concepts.',
        'credits': 3,
        'capacity': 25,
    },
    {
        'code': 'CSE310',
        'title': 'Web Engineering',
        'description': 'Server-side rendering, frontend integration, and responsive web design.',
        'credits': 4,
        'capacity': 20,
    },
]


def seed_courses(apps, schema_editor):
    Course = apps.get_model('registration', 'Course')
    for course_data in COURSES:
        Course.objects.get_or_create(code=course_data['code'], defaults=course_data)


def unseed_courses(apps, schema_editor):
    Course = apps.get_model('registration', 'Course')
    Course.objects.filter(code__in=[course['code'] for course in COURSES]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_courses, unseed_courses),
    ]
