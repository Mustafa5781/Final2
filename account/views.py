from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from account.forms import RegistrationForm, AccountAuthenticationForm
from django.contrib import messages


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                field_label = form.fields[field].label or field
                for error in errors:
                    messages.error(request, f"{field_label}: {error}")

                    
    else: #GET request
        form = RegistrationForm()
            
    context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')



def login_view(request):
    # If the user is already authenticated, redirect to "home"
    if request.user.is_authenticated:
        return redirect("main")
    
    context = {}
    
    if request.method == "POST":  # Process the login form on POST requests
        form = AccountAuthenticationForm(data=request.POST)  # Use `data` argument for better clarity
        if form.is_valid():
            email = form.cleaned_data.get('email')  # Use cleaned_data for safe access
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)  # Log the user in
                return redirect("home")  # Redirect to the "home" page
        else:
            for field, errors in form.errors.items():
                if field == '__all__':  # Handle non-field errors
                    for error in errors:
                        messages.error(request, f"Error: {error}")
                else:
                    field_label = form.fields[field].label or field
                    for error in errors:
                        messages.error(request, f"{field_label}: {error}")

            context['login_error'] = "Invalid credentials. Please try again."

            context['login_form'] = form
            return render(request, 'account/login.html', context)

    # else:
    form = AccountAuthenticationForm() 
    context['login_form'] = form
    return render(request, 'account/login.html', context)