from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile, Student, Teacher, Group, Schedule

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        Profile.objects.create(
            user=user,
            name=request.POST.get('name', '').strip() or user.username,
            lastname=request.POST.get('lastname', '').strip(),
            email=user.email
        )
        login(request, user)
        return redirect('dashboard')
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    profile = Profile.objects.filter(user=request.user).first()
    student = Student.objects.filter(profile=profile).first() if profile else None
    teacher = Teacher.objects.filter(profile=profile).first() if profile else None
    schedules = Schedule.objects.all().order_by('datetime')
    if student and student.group:
        schedules = schedules.filter(group=student.group)
    return render(request, 'accounts/dashboard.html', {
        'profile': profile,
        'student': student,
        'teacher': teacher,
        'students': Student.objects.select_related('profile', 'group').all(),
        'teachers': Teacher.objects.select_related('profile').all(),
        'groups': Group.objects.all(),
        'schedules': schedules,
    })
