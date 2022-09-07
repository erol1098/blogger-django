from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout

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


def user_logout(request):
    # messages.success(request,'You logged out!')
    logout(request)
    return redirect('index')