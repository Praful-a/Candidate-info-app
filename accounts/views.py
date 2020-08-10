from django.shortcuts import render, redirect
from .forms import UserAdminCreationForm

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
