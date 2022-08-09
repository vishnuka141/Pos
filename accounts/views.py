from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login,logout
from accounts.forms import SigninForm
from accounts.models import User
from django.urls import reverse_lazy
# Create your views here.


class SigninView(FormView):
    template_name = 'login.html'
    form_class = SigninForm
    # model=User
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            pwd=form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            user=authenticate(request,email=email,password=pwd)
            print(user)
            if user :

                login(request,user)
                return redirect('userhome')

        return render(request, 'login.html')

def logout_(request):
    logout(request)
    return render(request,'login.html')



def userhome(request):
    return render(request,'userhome.html')


