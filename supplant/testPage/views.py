from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import TestInput

# Create your views here.

def index(request):
  if request.method == "POST":
    form_response = TestInput(request.POST)

    if form_response.is_valid():
      data = form_response.cleaned_data["test_input"]
      print(data)
      return HttpResponse(data)
  else:
    form = TestInput()
    return render(request, "test.html", {"form":form})