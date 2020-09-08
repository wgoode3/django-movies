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

def color_selector(request):
    if "color" in request.session:
        print(request.session["color"])
    else:
        print("the key has not been set")
    return render(request, "color_selector.html")

def set_color(request):
    print(request.POST)
    request.session["color"] = request.POST["color"]
    return redirect("/colors")

def reset(request):
    request.session.clear()
    return redirect("/colors")