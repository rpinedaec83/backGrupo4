from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Product, Order, LineItem
from .forms import CartForm, CheckoutForm
from . import cart

def index(request):
    all_products = Product.objects.all()
    return render(request, "ecommerce_app/index.html", {'all_products': all_products})

def show_product(request, product_id, product_slug):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = CartForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            return redirect('show_cart')

    form = CartForm(request, initial={'product_id': product.id})
    return render(request, 'ecommerce_app/product_detail.html', {'product': product, 'form': form})

def show_cart(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'Update':
            cart.update_item(request)
        if request.POST.get('submit') == 'Remove':
            cart.remove_item(request)

    cart_items = cart.get_all_cart_items(request)
    cart_subtotal = cart.subtotal(request)
    return render(request, 'ecommerce_app/cart.html', {'cart_items': cart_items, 'cart_subtotal': cart_subtotal})

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            order = Order.objects.create(
                name=cleaned_data.get('name'),
                email=cleaned_data.get('email'),
                postal_code=cleaned_data.get('postal_code'),
                address=cleaned_data.get('address'),
            )
            cart_items = cart.get_all_cart_items(request)
            for cart_item in cart_items:
                LineItem.objects.create(
                    product=cart_item.product,
                    price=cart_item.price,
                    quantity=cart_item.quantity,
                    order=order
                )

            cart.clear(request)

            request.session['order_id'] = order.id

            messages.add_message(request, messages.INFO, 'Order Placed!')
            return redirect('checkout')
    else:
        form = CheckoutForm()
        return render(request, 'ecommerce_app/checkout.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm(request)
    return render(request, 'ecommerce_app/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'ecommerce_app/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')
