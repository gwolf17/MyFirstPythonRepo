from django.shortcuts import render


#Index Page route
def indexPageView(request):
    return render(request, 'MoviesApp/index.html')

#Display page route
def displayPageView(request):
    return render(request, 'MoviesApp/diplay.html')

#Show_Info route
def show_infoPageView(request):
    #data to be sent to the show_info.html page
    context = {
        "movie_title" : "galaxy quest",
        "movie_year" : "1999"
    }
    return render(request, 'MoviesApp/show_info.html', context)

#Show_Movie route
def show_moviePageView(request):
    #data to be sent to the show_movie.html page
    context = {
        "movie_title" : "galaxy quest"
    }
    return render(request, 'MoviesApp/show_movie.html', context)