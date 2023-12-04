from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    """ users registration form and validation """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your Account {} has been created. ready to Sign In!".format(username))
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
