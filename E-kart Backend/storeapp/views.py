from django.shortcuts import render,redirect,HttpResponse
from productapp.models import Product
from storeapp.models import Cart,Order
from django.db.models import Q
import random
import razorpay
from django.core.mail import send_mail

# Create your views here.
'''
views provise response to client by using:
1) HttpResponse()
2) render(request,'filename.html',data)
'''
# def homepage(request):
#     #return HttpResponse('Hello from Home Page')
#     context={}
#     context['msg']="Hello all, Good Morning!!!"
#     context['x']=1000
#     context['y']=200
#     context['data']=[10,20,30,40,50,60]
#     return render(request,'storeapp/home.html',context)

# def contactpage(request):
#     return HttpResponse('Hello from Contact Page')

# def aboutpage(request):
#     return HttpResponse('Hello from About Page')

# def edit(request,id):
#     print("ID to be edited:",id)
#     return HttpResponse("ID to be updated:"+id)

# def delete(request,id):
#     print("ID to be Delete:",id)
#     return HttpResponse("ID to be deleted:"+id)

# def addition(request,x,y):
#     res=int(x)+int(y)
#     print ("Addition is:",res)
#     return HttpResponse("Addition is:"+str(res))

def home(request):
#fetch available products from database
    p=Product.objects.filter(is_available=True)
    print(p)
    context={}
    context['pdata']=p
    return render(request,'storeapp/index.html',context)

def product_details(request,pid):
    #fetch product details with its id

        p=Product.objects.get(id=pid)
        #p=Product.objects.filter(id=pid
        print(p)
        context={}
        context['product']=p
        #send that fetched product details to product_details.html
        return render(request,'storeapp/product_details.html',context)

def about(request):
    return render(request,'storeapp/about.html')

def cart(request):
    #print("Value is:",request.user.is_authenticated)
    context={}
    if request.user.is_authenticated:
        #Fetch all cart product of logged in user
        #select* fromstoreapp_cart where uid=4
        c=Cart.objects.filter(uid=request.user.id)
        print(c)
        context['product']=c

        nos=len(c)
        total=0
        for x in c:
            total=total+(x.pid.price*x.qty)
        context['orders']=c
        context['n']=nos
        context['amt']=total
        return render(request,'storeapp/cart.html',context)
    else:
        return redirect('/accountapp/login')

def contact(request):
    return render(request,'storeapp/contact.html')

def cat_filter(request,catv):
    #print(catv)
    if request.user.is_authenticated:
        q1=Q(cat=catv)
        q2=Q(is_available=True)
        p=Product.objects.filter(q1&q2)
        context={}
        context['pdata']=p
        return render(request,'storeapp/index.html',context)
    else:
        return redirect('/accountapp/login')


def pricerange(request):
    context={}
    min=request.GET['min']
    max=request.GET['max']
    # print(min)
    # print(max)
    if not min.isdigit() or not max.isdigit():
        context['errmsg']="Value should be in digit"
        return render(request,'storeapp/index.html',context)
    elif int(min)<0 or int(max)<0:
        context['errmsg']="Value cannot be in Negative"
        return render(request,'storeapp/index.html',context)
    elif int(min)>int(max):
        context['errmsg']="Minimum cannot be greater than maximum value"
        return render(request,'storeapp/index.html',context)
    else:
        min=int(min)
        max=int(max)
        q1=Q(price__gte=min)
        q2=Q(price__lte=max)
        q3=Q(is_available=True)
        p=Product.objects.filter(q1&q2)
        context['pdata']=p
        return render(request,'storeapp/index.html',context)

def sort(request):
    qpara=request.GET['q']
    context={}
    # print(qpara)
    if qpara=='asc':
        #p=Product.objects.order_by('price').filter(is_available=True)
        x='price'
    else:
        #p=Product.objects.order_by('-price').filter(is_available=True)
        x='-price'
    p=Product.objects.order_by(x).filter(is_available=True)
    context['pdata']=p
    return render(request,'storeapp/index.html',context)

def search(request):
    x=request.GET['search']
    q1=Q(name__icontains=x)
    q2=Q(pdetails__icontains=x)
    p=Product.objects.filter(q1 | q2)
    context={'pdata':p}
    return render(request,'storeapp/index.html',context)

    #cart functionality
def addtocart(request,prod_id):
    #print(prod_id)
    context={}
    if request.user.is_authenticated:
        user_id=request.user.id
        pobj=Product.objects.get(id=prod_id)
        q1=Q(uid=user_id)
        q2=Q(pid=prod_id)
        check=Cart.objects.filter(q1&q2)
        #print(check)
        context['product']=pobj
        if len(check):
            context['msg1']="Product already Exists in Cart!!"
            return render (request,'storeapp/product_details.html',context)
        else:
            c=Cart.objects.create(uid=request.user,pid=pobj)
            c.save()
            context['msg2']="Product added successfully in Cart!!"
            return render (request,'storeapp/product_details.html',context)
    else:
        return redirect('/accountapp/login')

def remove_cart(request,cid):
    c=Cart.objects.get(id=cid)
    c.delete()
    return redirect('/cart')

def changeqty(request,cid):
    qparam=request.GET['q']
    # print(cid)
    # print(qparam)
    c=Cart.objects.filter(id=cid)
    print(c)
    print(c[0])
    x=c[0].qty
    if qparam=='plus':
        x=x+1
    else:
        if x>1:
            x=x-1

    c.update(qty=x)

    return redirect('/cart')
def generate_orderid():
    n=random.randrange(1000,9999)
    order_id='EK'+str(n)
    o=Order.objects.filter(order_id=order_id)
    if len(o)==0:
        return order_id
    else:
        generate_orderid()

def place_order(request):
    context={}
    if request.user.is_authenticated:
        oid=generate_orderid()
        #print(oid)
        c=Cart.objects.filter(uid=request.user.id)
        for x in c:
            o=Order.objects.create(order_id=oid,uid=x.uid,pid=x.pid,qty=x.qty)
            o.save()
            x.delete()

        q1=Q(uid=request.user.id)
        q2=Q(is_completed=False)
        o=Order.objects.filter(q1 & q2)
        nos=len(o)
        total=0
        for x in o:
            total=total+(x.pid.price*x.qty)
        context['orders']=o
        context['n']=nos
        context['amt']=total
        return render(request,'storeapp/place_order.html',context)
    else:
        return redirect('/account/login')

def cancelorder(request,oid):
    context={}
    o=Order.objects.filter(id=oid)
    o.delete()

    orem=Order.objects.filter(uid=request.user.id)
    context['orders']=orem
    return render(request,'storeapp/place_order.html',context)

def make_payment(request):
    context={}
    client = razorpay.Client(auth=("rzp_test_xSL5qfVsYB34iw", "ybcvNQJQA0oWUYbiiSW2J4p1"))
    #print(client)
    q1=Q(uid=request.user.id)
    q2=Q(is_completed=False)
    o=Order.objects.filter(q1 & q2)
    total=0
    for x in o:
        total=total+(x.pid.price*x.qty)

    famt=total*100
    data={"amount":famt,"currency":"INR","receipt":o[0].order_id}
    payment=client.order.create(data=data)
    print(payment)
    context['payment']=payment
    return render(request,'storeapp/pay.html',context)

def sendmail(request):

    order_id=request.GET['oid']
    pay_id=request.GET['rpayid']
    roid=request.GET['roid']
    # print(order_id)
    # print(pay_id)
    # print(roid)
    #updating order is_completed to 1
    o=Order.objects.filter(order_id=order_id)
    o.update(is_completed=True)

    subject="Ekart-Order Placed Successfully"
    msg="Order Details are: Order is-"+order_id+"Payment Id:"+pay_id
    #email send
    send_mail(
        subject,
        msg,
        "chiliverysravs@gmail.com",
        [request.user.email],
        fail_silently=False,
        )
    return HttpResponse("Mail has been sent")



#yaxf rhaq jrty lffn