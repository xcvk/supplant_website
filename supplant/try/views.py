from django.shortcuts import render
from .forms import GetInput
from django.http import HttpResponse
from .algorithm.algorithm_placeholder import algor

# Create your views here.
def index(request):
  if request.method == "POST":
    answer = GetInput(request.POST)

    if answer.is_valid():
      data = answer.cleaned_data["to_fix"]
      form = GetInput({"to_fix":data})
      result = algor(data)
    return render(request, 'try_filled.html', {"form":form, "result":result})

  else:
    form = GetInput({"to_fix":"hello"})
    return render(request, 'try.html', {"form":form})