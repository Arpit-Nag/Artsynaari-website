from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Product,ProductImage,Category,yarn,Slot,ProductRequest,Muses,MusesImage
from .forms import RequestForm
from accounts.models import Customer
from accounts.forms import UserAdminCreationForm




def product_list_view(request):
    category = request.GET.get('category')
    if category==None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__name=category)
    categories = Category.objects.all()
    slots = Slot.objects.all()
    return render(request,'store/product_list.html',{'products':products,'categories':categories,
                                                        'slots':slots})

def product_detail_view(request, pk):
    category = request.GET.get('category')
    if category==None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__name=category)
    categories = Category.objects.all()
    slots = Slot.objects.all()
    product= Product.objects.get(pk=pk)
    photos = ProductImage.objects.filter(product=product)
    yarns = yarn.objects.all()
    return render(request,'store/product_detail.html',{'product':product,'photos':photos,
    'categories':categories,'products':products,'slots':slots,'yarns':yarns})

def slotinfo(request):
    slots = Slot.objects.all()
    return render(request,'about_page.html',{'slots':slots})

@login_required
def Request_view(request, pk):
    product = get_object_or_404(Product,pk=pk)
    customer = request.user
    if request.method == 'POST':
        request_form = RequestForm(data=request.POST)
        if request_form.is_valid():
            request = request_form.save(commit=False)
            request.product=product
            request.customer=customer
            request.save()
            return redirect('store:request_summary',pk=request.pk)
    else:
        request_form=RequestForm()
    return render(request,'store/request_form.html',{'request_form':request_form,'product':product,})


def Request_Summary_view(request,pk):
    product_request = ProductRequest.objects.get(pk=pk)
    return render(request,'store/request_summary.html',{'product_request':product_request})

def Muses_view(request):
    guests = Muses.objects.all()
    images = MusesImage.objects.all()
    return render(request,'store/muses.html',{'guests':guests,'images':images})

def terms_view(request):
    return render(request,"terms.html")

def privacy_view(request):
    return render(request,"privacy.html")

def refund_policy_view(request):
    return render(request,'Refund_policy.html')

def contact_info_view(request):
    return render(request,'contact_info.html')
