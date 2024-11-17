from itertools import product

from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from shop.forms import ProductForm
from shop.models import Product


def base(request):
    return render(request,'base.html')

def home(request):
    products=Product.objects.all()
    print(products)
    return render(request,'home.html',{'products':products})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username=username,email=email,password=password1)
        myuser.firstname = fname
        myuser.lastname = lname
        myuser.save()
        return redirect('signin')
    return render(request, 'sighnup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            return render(request, 'user_dashboard.html', {'fname':fname, 'lname':lname})
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')
    return render(request, 'login.html')

def add_product(request):
    if request.method =='POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request,"Successfully added new product")
    product_form = ProductForm()
    return render(request, 'add_product.html',{'form':product_form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method=='POST':
        product_form = ProductForm(request.POST,request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')
        product_form = ProductForm(instance=product)
        return render(request, 'edit_product.html', {'form':product_form})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('home')
