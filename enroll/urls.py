from django.urls import path
from enroll import views

urlpatterns = [
    path('addstudent/', views.addAndShow, name="addstudent"),
    path('deletestudent/<int:student_id>/', views.deleteStudent, name="deletestudent"),
    path('editstudentform/<int:student_id>/', views.showEditStudentForm, name="editstudent"),
    path('updateStudent/', views.updateStudentDetails, name="updatestudent"),
]
