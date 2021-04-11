from django.shortcuts import render

def index(request):
    context = {
        "wdd_img": media/world_diety_database_logo.jpg
    }
    return render(request, "index.html", context)

def about_me(request):
    return render(request, "about_me.html")