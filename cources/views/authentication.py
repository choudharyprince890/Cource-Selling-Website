from django.http import HttpResponse
from django.shortcuts import redirect, render
from cources.models.cource import *
from cources.forms.registration_forms import RegistrationForm
from cources.forms.login_form import LoginForm
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == 'GET':
        form = RegistrationForm()
        context = {
            'form':form
        }
        return render(request, 'cources/signup.html', context)
    form = RegistrationForm(request.POST)
    if form.is_valid():
        user = form.save()
        if user:
            return redirect('login')
    return render(request, 'cources/signup.html',  context = {'form':form} )
    # elif request.method == 'POST':
    #     return HttpResponse('posrt')
        

def signin(request):
    if request.method == 'GET':
        login_form = LoginForm()
        login_context = {
            'login_form': login_form
        }
        return render(request, 'cources/login.html', login_context)
    else:
        login_form = LoginForm(request=request,data=request.POST)
        login_context = {
                'login_form': login_form
            }
        if login_form.is_valid():
            print('///////////////')
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print('username is ....',username)
            print('password is ....',password)
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user) 
                return redirect('index')
        print('not done')
        return render(request, 'cources/login.html', login_context)

        
def signout(request):
    logout(request)
    return redirect('index')