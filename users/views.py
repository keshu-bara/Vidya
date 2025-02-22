from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
    '''log the user out'''
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

def register(request):
    '''Here the registration for new user'''
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        #Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #log the user in then redirect to home page
            authenticate_user = authenticate(username=new_user.username,password=request.POST['password1'])
            if authenticate_user is not None:
                login(request, authenticate_user)
                return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {
        'form':form,
    }
    return render(request,'users/registration.html',context)

