from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


# Login view
def user_login(request):
    if request.method == "POST":
        # Instantiate the form with the submitted data with form = LoginForm(request.POST).
        form = LoginForm(request.POST)
        # Check whether the form is valid with form.is_valid(). If it is not valid, you display
        # - the form errors in your template (for example, if the user didn't fill in one of the fields).
        if form.is_valid():
            cd = form.cleaned_data
            # Authenticate the user against the database using the authenticate() method.
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password']
                                )
            if user is not None:
                # If user is registered and active log user in
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')

                else:
                    # If user account is disabled
                    return HttpResponse('Disabled account')
            else:
                # If there user account does not exist
                return HttpResponse('Invalid login')
    else:
        # Return clean form
        form = LoginForm()
    return render(request, 'account/login.html', {
        'form': form
    })


# Dashboard view
# Check if current user is authenticated
@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {
                      'section': 'dashboard'
                  })
