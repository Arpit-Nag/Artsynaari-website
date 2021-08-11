from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm
from store.models import ProductRequest,Slot
from django.contrib.auth.decorators import login_required

def Register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def user_homepage_view(request):
    customer = request.user
    purchases = ProductRequest.objects.filter(customer=customer)
    slots = Slot.objects.all()
    return render(request,'accounts/home.html',{'customer':customer,'purchases':purchases,'slots':slots})
