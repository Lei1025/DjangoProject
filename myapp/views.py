from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from myapp.models import Author, Book, Course, Topic, Student
from myapp.forms import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    courselist = Course.objects.all().order_by('title')[:10]
    return render(request, 'myapp/index.html', {'courselist': courselist})


def about(request):
    return render(request, 'myapp/about.html')


def detail(request, course_No):
    get_object_or_404(Course, course_no=course_No)
    course = Course.objects.get(course_no=course_No)
    return render(request, 'myapp/detail.html', {'course': course})


def topics(request):
    topiclist = Topic.objects.all()
    return render(request, 'myapp/topics.html', {'topiclist': topiclist})


def addtopic(request):
    topiclist = Topic.objects.all()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.num_responses =+ 1
            topic.save()
            return HttpResponseRedirect(reverse('myapp:topics'))
    else:
        form = TopicForm()
    return render(request, 'myapp/addtopic.html', {'form': form, 'topiclist': topiclist})

def topicdetail(request, topic_id):
    get_object_or_404(Topic, subject=topic_id)
    topic = Topic.objects.get(subject=topic_id)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.cleaned_data['interest']
            age = form.cleaned_data['age']
            topic.avg_age = (topic.num_responses * topic.avg_age + age) / (topic.num_responses + 1)
            if interest:
                topic.num_responses = +1
                topic.save()
        return HttpResponseRedirect(reverse('myapp:topics'))
    else:
        form = InterestForm()
        return render(request, 'myapp/topicdetail.html', {'topic': topic, 'form': form})

def register(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password1']
        password2=request.POST['Password2']
        firstname=request.POST['Firstname']
        lastname = request.POST['Lastname']
        email = request.POST['Email']
        if password!=password2:
            return HttpResponse('Password not match!')
        elif password==password2:
            Student.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
            return HttpResponseRedirect(reverse('myapp:login'))
    else:
        return render(request,'myapp/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index')) #
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('myapp:index')))

@login_required()
def mycourse(request):
    try:
        Student.objects.get(username=request.user)
        course=Course.objects.filter(students__username=request.user)
        return render(request, 'myapp/mycourse.html',{'user':request.user,'course':course})
    except:
        return HttpResponse('You are not a student!')
    return render(request,'myapp/mycourse.html')

def fotgetPassword(request):
    try:
        pass
    except:
        return render(request,'myapp/ForgetPassword.html')
    return render(request, 'myapp/ForgetPassword.html')

    '''
if request.method=='POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            interest=form.cleaned_data['interest']
            age=form.cleaned_data['age']
            topic.avg_age = (topic.num_responses*topic.avg_age+age)/(topic.num_responses+1)
            if interest:
                topic.num_responses=+1
                topic.save()
            return HttpResponseRedirect("/topics/page")
    else:
        form=InterestForm()
    return render(request, 'myapp/topicdetail.html', {'topic':topic,'form':form})


def index(request):
    courselist = Course.objects.all() [:10]
    response = HttpResponse()
    heading1 = '<p>' + 'List of courses: ' + '</p>'
    response.write(heading1)
    for course in courselist:
        para = '<p>' + str(course) + '\t-- Course No.'+ str(course.course_no) + '</p>'
        response.write(para)
    authorlist = Author.objects.all().order_by('-birthdate')[:5]
    heading2 = '<p>' + 'List of Authors: ' + '</p >'
    response.write(heading2)
    for author in authorlist:
        para = '<p>' + str(author) + '\t-- Birthdate: ' + str(author.birthdate)+ '</p >'
        response.write(para)
    return response


def about(request):
    response=HttpResponse()
    text='<p>'+'This is a Course Listing APP'+'</p>'
    response.write(text)
    return response
    
def detail(request, course_No):
    response=HttpResponse()
    get_object_or_404(Course, course_no=course_No)
    str1='<p>' + 'Information of courses: ' + '</p>'
    response.write(str1)
    course=Course.objects.filter(course_no=course_No)
    for i in course:
        response.write("<p>" + str(i) + "</p>")
        response.write("<p>" + "Course Numver: " + str(course_No) + "</p>")
        response.write("<p>" + "TextBook: " + str(i.textbook) + "</p>")
    return response
'''
