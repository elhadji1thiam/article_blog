from django.contrib.auth import login, logout,authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Vue pour le login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    
    return render(request, 'utilisateur/login.html', {'form': form})

# Vue pour le logout
def logout_view(request):
    logout(request)
    return redirect('/')

# Vue pour le signup (inscription)
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('list_article')
    else:
        form = UserCreationForm()
    
    return render(request, 'utilisateur/signup.html', {'form': form})
