from django.shortcuts import render, redirect
from .forms import Userform


def signup(request):
    formz = Userform
    if request.method == 'POST':
        formz = Userform(request.POST)
        if formz.is_valid():
            formz.save()
            return redirect('displaypage')
    return render(request, 'myapp/signup.html', {'formz': formz})
