from django.shortcuts import render, reverse, redirect
from section.forms import RegistrationForm
from django.contrib.auth.models import User

def home(request):
    return render(request,'section/home.html')

def register(request):
    if  request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():        
            form.save()
            print('data has been saved')
            return redirect(reverse('home_page'))

    form = RegistrationForm()
    args={'form':form}
    return render(request,'section/reg_form.html',args)
