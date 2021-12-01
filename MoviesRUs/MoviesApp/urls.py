from django.urls import path
from .views import displayPageView, indexPageView, show_infoPageView, show_moviePageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("show_info/", show_infoPageView, name="show_info"),
    path("show_movie/", show_moviePageView, name="show_movie"),
    path("display/", displayPageView, name="display")
]