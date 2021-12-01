from django.urls import path
from .views import indexPageView, aboutPageView
from .views import studentPageView, searchEmpPageView

urlpatterns = [
    path("about/<str:trip_name>/<int:trip_length>", aboutPageView, name="about"),
    path("stud/", studentPageView, name="student"),
    path("searchemp/", searchEmpPageView, name="searchemp"),
    path("", indexPageView, name="index"),
]
