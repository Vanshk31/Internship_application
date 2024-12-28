# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
from .forms import StudentRegistrationForm

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        # Checking if form submission (regular HTML form) or API JSON request
        if request.content_type == 'application/x-www-form-urlencoded':
            # Handling form submission (HTML)
            username = request.POST.get('username')
            password = request.POST.get('password')
        elif request.content_type == 'application/json':
            # Handling API JSON request
            try:
                data = json.loads(request.body)
                username = data.get('username')
                password = data.get('password')
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        else:
            return JsonResponse({'error': 'Unsupported content type'}, status=400)

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.content_type == 'application/x-www-form-urlencoded':
                return redirect('/')  # redirect to home page after login
            else:
                return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            if request.content_type == 'application/x-www-form-urlencoded':
                return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)

    return render(request, 'accounts/login.html')
