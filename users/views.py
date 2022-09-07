from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.forms import ProfileForm, UserForm

# Create your views here.

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            # messages.success(request, "Login Successfull")
            login(request,user)
            return redirect('index')

    return render(request, 'users/user_login.html', {"form":form})

def register(request):
    
    if request.method == 'POST':
      
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
      
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
          
            user = authenticate(username=username, password=password)
            
        
            login(request, user)
         
            return redirect('index')
            
    else:
        form = UserCreationForm()
    
    ctx = {
        'form': form
    }
    
    return render(request, "users/register.html", ctx)

@login_required(login_url='/user/login/')
def user_logout(request):
    # messages.success(request,'You logged out!')
  logout(request)
#   return redirect("index")
  return render(request, "users/logout.html")

@login_required(login_url='/user/login/') 
def profile(request):
    profileForm = ProfileForm()

    if request.method == "POST":
        profileForm = ProfileForm(request.POST, request.FILES, )
        if profileForm.is_valid():
            profileForm.save()
            return redirect("/user/profile")

    ctx = {"form":profileForm,}
    
    return render(request, "users/profile.html", ctx)