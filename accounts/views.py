from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserAdminCreationForm, UserLoginForm

# Create your views here.
def register(request, *args, **kwargs):
    form = UserAdminCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('account:login')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return redirect('candidate:home')
    return render(request, "accounts/login.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect('account:login')
