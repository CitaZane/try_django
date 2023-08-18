from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>Hello world</h1>") # string html code
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about me",
        "my_number": 123,
        "my_list": [1,2,3,5]
    }
    return render(request, "about.html", my_context)