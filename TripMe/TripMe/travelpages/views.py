from django.shortcuts import render
from django.http import HttpResponse
from .models import Grade_Level, Student

def searchEmpPageView(request) :
    sFirst = request.GET['first_name']
    sLast = request.GET['last_name']
    sGrade_Level = request.GET['grade_level']

    sQuery = 'SELECT Student.id, first_name, last_name, description FROM Student, Grade_Level WHERE Student.class_level_id = Grade_Level.class_level'

    if sFirst != '' :
        sQuery += " AND first_name = '" + sFirst + "'"
        
    if sLast != '' :
        sQuery += " AND last_name = '" + sLast + "'"

    if sGrade_Level != '' :
        sQuery += " AND class_level_id = '" + sGrade_Level + "'"        

    sQuery += ' ORDER BY first_name, last_name, description'

    data = Student.objects.raw(sQuery)

    lookup = Grade_Level.objects.all()

    context = {
        "our_students" : data,
        "grades" : lookup,
    }

    return render(request, 'travelpages/displayStudents.html', context)

# Create your views here.
def studentPageView(request) :
    data = Student.objects.all()
    lookup = Grade_Level.objects.all()

    context = {
        "our_students" : data,
        "grades" : lookup,
    }

    return render(request, 'travelpages/displayStudents.html', context)

def indexPageView(request) :
    return render(request, 'travelpages/index.html',)

def aboutPageView(request, trip_name, trip_length) :

    context = {
        "trip_name" : trip_name,
        "trip_length" : trip_length + 2,
        "places_to_visit" : ["Arenal Volcano", "Manual Antonio National Park", "Monteverde Cloud Forest"]
    } 

    return render(request, 'travelpages/about.html', context)