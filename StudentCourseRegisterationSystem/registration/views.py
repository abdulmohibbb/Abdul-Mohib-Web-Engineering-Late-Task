from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import StudentRegistrationForm
from .models import Course, Enrollment, StudentProfile


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            StudentProfile.objects.create(
                user=user,
                student_id=form.cleaned_data['student_id'],
                phone=form.cleaned_data['phone'],
                major=form.cleaned_data['major'],
            )
            login(request, user)
            messages.success(request, 'Registration completed successfully.')
            return redirect('dashboard')
    else:
        form = StudentRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    profile = request.user.student_profile
    enrolled_courses = Course.objects.filter(enrollments__student=profile).distinct()
    available_courses = Course.objects.exclude(enrollments__student=profile).order_by('code')
    return render(
        request,
        'registration/dashboard.html',
        {
            'profile': profile,
            'enrolled_courses': enrolled_courses,
            'available_courses': available_courses,
            'enrollment_total': Enrollment.objects.filter(student=profile).count(),
        },
    )


@login_required
def course_list(request):
    profile = request.user.student_profile
    courses = Course.objects.all().prefetch_related('enrollments')
    enrolled_course_ids = set(
        Enrollment.objects.filter(student=profile).values_list('course_id', flat=True)
    )
    return render(
        request,
        'registration/courses.html',
        {
            'courses': courses,
            'enrolled_course_ids': enrolled_course_ids,
        },
    )


@login_required
@require_POST
def enroll_course(request, course_id):
    profile = request.user.student_profile
    course = get_object_or_404(Course, pk=course_id)

    if Enrollment.objects.filter(student=profile, course=course).exists():
        messages.info(request, 'You are already enrolled in this course.')
        return redirect('courses')

    if course.available_seats <= 0:
        messages.error(request, 'This course is full.')
        return redirect('courses')

    try:
        with transaction.atomic():
            Enrollment.objects.create(student=profile, course=course)
    except IntegrityError:
        messages.error(request, 'Could not complete enrollment. Please try again.')
    else:
        messages.success(request, f'Enrolled in {course.code}.')
    return redirect('courses')


@login_required
@require_POST
def drop_course(request, enrollment_id):
    profile = request.user.student_profile
    enrollment = get_object_or_404(Enrollment, pk=enrollment_id, student=profile)
    course_title = enrollment.course.code
    enrollment.delete()
    messages.success(request, f'Dropped {course_title}.')
    return redirect('courses')
