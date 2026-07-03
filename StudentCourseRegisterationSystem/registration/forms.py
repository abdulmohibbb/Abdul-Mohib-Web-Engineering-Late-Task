from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import StudentProfile


class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    student_id = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=20, required=False)
    major = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'student_id', 'phone', 'major', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user with this email already exists.')
        return email

    def clean_student_id(self):
        student_id = self.cleaned_data['student_id'].strip()
        if StudentProfile.objects.filter(student_id__iexact=student_id).exists():
            raise forms.ValidationError('A student with this ID already exists.')
        return student_id


class StudentLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
