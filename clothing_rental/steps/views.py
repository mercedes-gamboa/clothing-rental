from django.shortcuts import render

# Create your views here.
def how_it_works(request):
    return render(request, 'steps/steps.html')