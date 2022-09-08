from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


from .forms import CreateUserForm, ProfileForm, UpdateUserProfileForm
from .models import Profile
# Create your views here.

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            messages.success(request, "Login Successfull")
            login(request,user)
            return redirect('index')
 
    return render(request, 'users/user_login.html', {"form":form})

def register(request):
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
      
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
          
            user = authenticate(username=username, password=password)
            
            profile = Profile()
            profile.user = user
            profile.save()

            login(request, user)
         
            return redirect('index')
            
    else:
        form = CreateUserForm()

    
    ctx = {
        'form': form
    }
    
    return render(request, "users/register.html", ctx)

@login_required(login_url='/user/login/')
def user_logout(request):
    messages.success(request,'You logged out!')
    logout(request)
    return render(request, "users/logout.html")

@login_required(login_url='/user/login/') 
def profile_page(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)

    profileForm = ProfileForm(instance=profile)
    form = UpdateUserProfileForm(instance=user)

    if request.method == "POST":
        profileForm = ProfileForm(request.POST, request.FILES,instance=profile)
        form = UpdateUserProfileForm(request.POST, request.FILES,instance=user)

        if profileForm.is_valid():

            
           
            avatar = profileForm.cleaned_data['avatar']
            bio = profileForm.cleaned_data['bio']

            profile.bio = bio
            profile.avatar = avatar
            profile.save()
            
            if form.is_valid():
                form.save()
                return redirect(f"/user/profile/{id}")

    ctx = {"form":profileForm, "form1":form, "profile":profile}
    
    return render(request, "users/profile.html", ctx)