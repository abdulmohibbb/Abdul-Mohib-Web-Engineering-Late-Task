from django.contrib import admin

from .models import Course, Enrollment, StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'user', 'major', 'phone', 'created_at')
    search_fields = ('student_id', 'user__username', 'user__email', 'major')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'credits', 'capacity', 'enrolled_students_count')
    search_fields = ('code', 'title')
    list_filter = ('credits',)

    def enrolled_students_count(self, obj):
        return obj.enrollments.count()

    enrolled_students_count.short_description = 'Enrolled Students'


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    search_fields = ('student__student_id', 'student__user__username', 'course__code')
    list_filter = ('enrolled_at',)
