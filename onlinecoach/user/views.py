#Created by Mohsin Braer on May 25th 2019
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse 

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # return redirect(request.build_absolute_uri("/q"))
            return HttpResponseRedirect(reverse('qa:index'))
    else: 
        form = UserCreationForm()
        
    return render(request, 'user/register.html', {'form': form})

def index(request):
    return render(request, 'user/index.html')