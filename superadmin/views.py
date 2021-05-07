from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


from adminuser.models import Adminuser

@login_required
def superadmin_dashboard(request):
    return render(request,'superadmin/dashboard.html')


def create_user(request):
    if request.method == "POST":
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone_number']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if pass1 == pass2:
            if Adminuser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please try again')
                return redirect('create_user')
            else:
                if Adminuser.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists. Please try again')
                    return redirect('create_user')
                else:
                    user=User.objects.create(first_name=f_name,last_name=l_name,username=username,email=email,password=pass1)
                    admin = Adminuser.objects.create(first_name=f_name,last_name=l_name,username=username,email=email,phone_number=phone,created_by=user)
                    messages.success(request, 'Admin Account Successfully Created')
                    return redirect('create_user')
        else:
            messages.error(request,'Password not match. Please try again')
            return redirect('create_user')
    else:
        return render(request,'superadmin/user/createUser.html')


def admin_user_list(request):
    return render(request, 'superadmin/user/adminUserList.html')

def get_all_admin(request):
    start = int(request.POST.get('start', 0))
    end = int(request.POST.get('length', 20))
    queryset = Adminuser.objects.filter()
    return queryset


