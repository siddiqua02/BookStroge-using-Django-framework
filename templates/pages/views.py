from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    # return HttpResponse('<h1>hello world</h1>')
    return render(request,'pages/index.html')

def aboutus(request):
    # return HttpResponse('aboutus')
    # name = 'John'
    student = {
        1: 'murti',
        2: 'mg',
        3: 'anju',
        4: 'swati   '
    }
    results = {
        1 : {"name" : "john" , "cgpa": [9.2,8.3,9.4,9.7]},
        2 : {"name" : "swati" , "cgpa": [9.3,8.4,9.4,9.7]},
        3 : {"name" : "archie" , "cgpa": [9.4,8.5,9.4,9.7]},
        4 : {"name" : "anju" , "cgpa": [9.5,8.6,9.4,9.7]},
        5 : {"name" : "murti" , "cgpa": [9.6,8.7,9.4,9.7]}
    }
    context = {
        # 'name' : 'sam',
        'age' : 20,
        'num1' : 12,
        'num2' : 10,
        'nums' : [1,2,3,4,3,2,3],
        'students' : student,
        'results' : results
    }
    return render(request, 'pages/about.html', context)

def form(request):
    form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request,'pages/form.html',context)


