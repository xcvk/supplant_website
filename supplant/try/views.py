from django.shortcuts import render
from .forms import GetInput
from django.http import HttpResponse
from .supplant_logic.algorithm_placeholder import algor

def index(request):
  # if method is post, then user has sent some data. Change the resulting page.
  if request.method == "POST":
    answer = GetInput(request.POST)

    if answer.is_valid():
      data = answer.cleaned_data["to_fix"]
      form = GetInput({"to_fix":data})
      # fix the data here
      result = algor(data)
    return render(request, 'try_filled.html', {"form":form, "result":result})

  else:
    form = GetInput({"to_fix":"type here"})
    return render(request, 'try.html', {"form":form})