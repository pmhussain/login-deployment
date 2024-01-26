from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def login_view(request):
    logout_view(request)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            #user exist in User's, authenticate password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, "Password is not Valid")
        else:
            print("No user")
            messages.info(request, "Username does not exist")
    return render(request, 'loginApp/login.html')

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
        else:
            print(form.errors)
    return render(request, 'loginApp/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    msg=''
    if request.method == 'POST':
        print(request.POST)
        mobileno = "+91" + str(request.POST.get('mobileno'))
        message = request.POST.get('message')
        from datetime import datetime
        now = datetime.now()
        current_time_hrs = int(now.strftime("%H"))
        current_time_minutes = int(now.strftime("%M"))+2
        # current_time_seconds = int(now.strftime("%S"))

        import pywhatkit
        try:
             # pywhatkit.sendwhatmsg(mobileno, message, 22, 46)

             pywhatkit.sendwhatmsg(mobileno, message, current_time_hrs, current_time_minutes, 15, True, 2)
             msg = 'message sent sucessfully'
        except Exception as e:
            print('Error while sending message')
            print(e)

    return render(request, 'loginApp/welcome.html',{'msg':msg})
