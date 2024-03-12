from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import FeedingForm
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
   feeding_form = FeedingForm()
   return render(request, 'finches/details.html', {
      'finch': finch, 'feeding_form': feeding_form})


def add_feeding(request, finch_id):
   form = FeedingForm(request.POST)
   if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.finch_id = finch_id
      new_feeding.save()
   return redirect('details', finch_id=finch_id)



class FinchCreate(CreateView):
   model = Finch
   fields = '__all__'

class FinchUpdate(UpdateView):
   model = Finch
   fields = '__all__'

class FinchDelete(DeleteView):
   model = Finch
   success_url = '/finches'
