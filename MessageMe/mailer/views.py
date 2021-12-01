from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Welcome to ABC Company!')

def aboutPageView(request) :
    return HttpResponse('Mission Statement:\nWe are dedicated to doing important things and helping individuals fulfill their dreams.')

def contactPageView(request, name, email) :
    return HttpResponse("Welcome to ABC company " + name + "! We will send an email to " + email + " with more information. Thank you!")