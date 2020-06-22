from django.shortcuts import render, redirect
from home.models import Book
from .models import Cart, Order
from django.contrib import messages
from django.core.mail import send_mail
from obs.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone

def book_page(request,id):
    book_details = Book.objects.get(id = id)
    discount = int(book_details.price * 100 / 80)
    return render(request,'book/bookpage.html',{'details':book_details,'discount':discount})

def add_to_cart(request,book_id):
    print("ID is: ",book_id)
    user = request.user
    book = Book.objects.get(id = book_id)
    q = Cart(user = user,book_title = book)
    try:
        q.save()
    except:
        messages.error(request,f'Item {book.title} not added')
    else:
        messages.success(request,f'Item {book.title} added to the cart')

    cart_items = Cart.objects.filter(user = user)

    return render(request,'book/cart.html',{'cart_items': cart_items})

def cart(request):
    cart = Cart.objects.filter(user = request.user)
    return render(request, 'book/cart.html',{'cart_items':cart})

def bill(request,book_id):
    if (book_id==0):
        bill = Cart.objects.filter(user = request.user)
        sum = 0
        for b in bill:
            sum = sum + b.book_title.price
        Cart.objects.filter(user = request.user).delete()

        for i in bill:
            query = Order(user = request.user,book_title = i.book_title)
            query.save()
    else:
        bill = Book.objects.filter(id = book_id)
        sum = bill[0].price

        query = Order(user = request.user,book_title = bill[0])
        query.save()

    sendmail('Online Book Store','',request.user.email,bill=bill,sum=sum,time = timezone.localtime())
    
    return render(request,'book/bill.html',{'bill':bill,'sum':sum})

def orders(request):
    result = Order.objects.filter(user = request.user)
    return render(request,'book/orders.html', {'items':result} )

def sendmail(subject,message,recipient,bill,sum,time):

    html_message = render_to_string('book/email.html',{'bill':bill,'sum':sum,'time':time})
    send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently = False,html_message=html_message)
