from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "portfolio/index.html")
    

    
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "portfolio/index.html")
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/index.html', {'form': form})
