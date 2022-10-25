from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student, Department, Register, Staff
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


""" Displays the main page containing all links"""


def main(request):
    return render(request, 'students/main.html')


""" Displays the Student application page where student has to apply """


def application(request):
    return render(request, 'students/application.html')


""" Saves all the details provided by student in application """


def save(request):
    Student.objects.create(student_name=request.POST['name'], student_email=request.POST['Email'],
                           student_phone=request.POST['Phone'], ssc_marks=request.POST['ssc_marks'],
                           inter_marks=request.POST['inter_marks'])
    return HttpResponseRedirect('/students/')


""" Displays the Registration HTML page """


def registration(request):
    deps = Department.objects.all()
    return render(request, 'students/registration.html', {"deps": deps})


""" Saves all the details of the registration page """
""" If not valid redirects to application page """


def save_details(request):
    if Student.objects.filter(student_email=request.POST['email'], is_verified=True).exists():
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        student = Student.objects.get(student_email=request.POST["email"])
        dep = Department.objects.get(code=request.POST['code'])
        Register.objects.create(image=request.FILES['image'], department=dep, user=user, Student=student)
        return HttpResponseRedirect('/students/')
    else:
        return render(request, 'students/application.html', {'error': 'you are not a valid user'})


""" Displays the Student Login page """


def login_user(request):
    return render(request, 'students/login.html')


""" Validates the login credentials """


def validate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if User is not None:

        login(request, user)
        return HttpResponseRedirect('/students/details/')
    else:
        return render(request, 'students/login.html', {'error': 'Invalid username or password'})


""" Displays the details of the student logged in """


@login_required(login_url="/students/login/")
def details(request):
    user = request.user
    return render(request, 'students/details.html', {'user': user})


""" Redirects the student to login page after clicking on logout """


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/students/login/')


""" Displays the Staff Registration page """


def staff_registration(request):
    deps = Department.objects.all()
    return render(request, 'students/staff.html', {"deps": deps})


""" Saves the details of staff provided in registration page """


def save_staffdetails(request):
    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    Staff.objects.create(staff_name=request.POST['name'], staff_email=request.POST['email'],
                         staff_phone=request.POST['phone'], qualification=request.POST['qualification'],
                         staff_department=Department.objects.get(code=request.POST['code']),
                         experience=request.POST['experience'], image=request.FILES['image'], user=user)
    return HttpResponseRedirect('/students/')


""" Validates the details of the staff and register  """


def staff_validate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        if Staff.objects.filter(user=user).exists():
            return HttpResponseRedirect('/students/staff_details/')
    else:
        return render(request, 'students/staff.html', {'error': 'you are not a valid user'})


""" Displays the staff login page """


def staff_login(request):
    return render(request, 'students/staff_login.html')


""" Details of the staff logged in """


@login_required(login_url='/students/staff_login.html')
def  \staff_detail(request):
    user = request.user
    return render(request, 'students/staff_details.html', {'user': user})


""" Redirects the staff to login page after clicking on logout """


def staff_logout(request):
    logout(request)
    return HttpResponseRedirect('/students/staff_login/')


""" Displays all the details of staff """


@login_required(login_url="/students/staff_login/")
def total_staff(request):
    staff = Staff.objects.all()
    return render(request, 'students/total_staff.html', {'staff': staff})


""" Displays all the details of students in all departments """


@login_required(login_url="/students/login/")
def total_students(request):
    deps = Department.objects.all()
    return render(request, 'students/total_students.html', {"deps": deps})


""" Displays all the details of students in a particular department """


def std_details(request, dep_code):
    student = Register.objects.filter(department__code=dep_code)
    return render(request, 'students/mech_students.html', {'student': student})
