from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,"generator/index.html")

def password(request):
    characters = list("1234567890")
    
    length = int(request.GET.get("length"))
    
    if request.GET.get("characters"):
        characters.extend(list("1234567890"))
        
    password = ""
    for x in range(length):
        password = password + random.choice(characters)
    return render(request,"generator/password.html",{"password":password})