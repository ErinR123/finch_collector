from django.shortcuts import render
from .models import Finch
# Create your views here.



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  # Like in Express, we pass the request, the path to the template, and the data needed as a dictionary, to `render`
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_details(request, finch_id):
   finch = Finch.objects.get(id=finch_id)
   return render(request, 'finches/details.html', {'finch': finch})
