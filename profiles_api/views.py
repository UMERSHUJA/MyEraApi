from django.shortcuts import render, redirect
from django.contrib import messages, auth
from startup.models import Startup
from joblist.models import JobList
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        image = request.POST['profile_image']
        # check passwords are same 
        if password == password2:
            # check username
            if User.objects.filter(user_name=user_name).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Look good
                    user = User(user_name=user_name, email=email, password=password, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'profile/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'profile/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        startups = Startup.objects.order_by('submission_date').filter(published=False, user_id = request.user.id)
        startup_published = Startup.objects.order_by('submission_date').filter(published=True, user_id = request.user.id)
        joblists = JobList.objects.order_by('submission_date').filter(published=False, user_id = request.user.id)
        joblist_published = JobList.objects.order_by('submission_date').filter(published=True, user_id = request.user.id)
        
        context = {
            'startups': startups,
            'startup_published': startup_published,
            'joblists': joblists,
            'joblist_published': joblist_published
        }
        return render(request, 'profile/dashboard.html', context)
    else:
        return redirect('login')




def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
    
