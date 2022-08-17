from cProfile import label
from socket import fromshare
from django import forms
from enroll.models import Student
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ('studentName', 'studentEmail', 'studentPassword')
        labels = {'studentName': 'Student Name ',
                  'studentEmail':'Student Email ',
                  'studentPassword': 'Student Password '}
        widgets = {'studentName': forms.TextInput(attrs={'class':'inputfield',
        'placeholder':"Enter Student's Name"}),
        'studentEmail': forms.EmailInput(attrs={'class':'inputfield',
        'placeholder':"Enter Student's Email"}),
        'studentPassword': forms.PasswordInput(render_value=True, attrs={'class':'inputfield',
        'placeholder':"Enter a strong password"})}

    