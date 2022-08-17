from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

def addAndShow(request):
    if request.method == 'POST':
        formObject = StudentRegistration(request.POST)
        if formObject.is_valid():           
            newStudent = Student()
            newStudent.studentName = formObject.cleaned_data['studentName']
            newStudent.studentEmail = formObject.cleaned_data['studentEmail']
            newStudent.studentPassword = formObject.cleaned_data['studentPassword']
            newStudent.save() 
            return HttpResponseRedirect('http://localhost:8000/')
    else:
        formObject = StudentRegistration()
    allStudentsList = Student.objects.all()
    context = {"form":formObject, 'students':allStudentsList}
    response = render(request, 'enroll/addAndShow.html', context)
    return HttpResponse(response)

def showEditStudentForm(request, student_id):
    studentToBeUpdated = Student.objects.get(id=student_id)
    formObject = StudentRegistration(instance=studentToBeUpdated)
    context = {'form':formObject, 'studentid':student_id} 
    response = render(request, 'enroll/editstudentform.html', context)
    return HttpResponse(response)

def updateStudentDetails(request):
    studentToBeUpdated = Student.objects.get(id=int(request.POST['id']))
    formObject = StudentRegistration(request.POST, instance=studentToBeUpdated)
    if formObject.is_valid():
        formObject.save()
    return HttpResponseRedirect('http://localhost:8000/') 
 
def deleteStudent(request, student_id):
    studentToBeDeleted = Student.objects.get(id=student_id)
    studentToBeDeleted.delete()
    return HttpResponseRedirect('http://localhost:8000/') 
