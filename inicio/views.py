from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['id'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'Inicio/inicios.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'Inicio/inicios.html', {'form': form})