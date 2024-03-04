from django.shortcuts import render

# Create your views here.
finches = [
  {'name': 'sweetums', 'description': 'little demon', 'age': 3},
  {'name': 'Sachi', 'description': 'gentle and loving', 'age': 2},
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  # Like in Express, we pass the request, the path to the template, and the data needed as a dictionary, to `render`
  return render(request, 'finches/index.html', {
    'finches': finches
  })
