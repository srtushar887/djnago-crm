from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from superadmin.models import Superadmin
def user_login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if Superadmin.objects.filter(username=username).exists():
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('superadmin_dashboard')
            else:
                return redirect('user_login_page')
        else:
            return redirect('user_login_page')

    else:
        return render(request,'pages/userLogin.html')



def user_login_register(request):
    if request.method == 'POST':
        first_name = "superadmin"
        last_name = "superadmin"
        username = "superadmin"
        email = "superadmin@gmail.com"
        password = "12345678"

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name)

        superadmin = Superadmin.objects.create(username=username, email=email, first_name=first_name,last_name=last_name,created_by=user)


    else:
        return render(request, 'pages/userRegister.html')
