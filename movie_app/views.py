from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, "index.html")

def movie_suggestion(request):
    print(request.POST)
    context = {
        "title": request.POST["title"],
        "year": request.POST["year"],
        "rating": request.POST["rating"]
    }
    # context = {"data": request.POST}
    return render(request, "results.html", context)

def get_time(request):
    context = {
        "currentDay": datetime.strftime(datetime.now(), "%B the %-dth, %Y"),
        "currentTime": datetime.strftime(datetime.now(), "%-I:%M:%S %p")
    }
    return render(request, "time.html", context)