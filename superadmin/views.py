from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def superadmin_dashboard(request):
    return render(request,'superadmin/dashboard.html')
