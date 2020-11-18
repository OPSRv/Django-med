from django.shortcuts import render
from covid19.models import covid19

def home(request):
    covid19_data = covid19.objects.all()
    context = {
        'covid19': covid19_data
    }
    return render(request, "pages/index.html", context)
