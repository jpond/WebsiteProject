from django.shortcuts import render
from .models import *
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, "home.html", {})
    
    def post(self, request):
        return render(request, "home.html", {})

class Projects(View):
    def get(self, request):
        return render(request, "projects.html", {})

    def post(self, request):
        return render(request, "projects.html", {})

class Resume(View):
    def get(self, request):
        return render(request, "resume.html", {})

    def post(self, request):
        return render(request, "resume.html", {})
