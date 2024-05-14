from django.shortcuts import render,HttpResponse,redirect
from productapp.models import Product
# Create your views here.
def homepage(request):
    return HttpResponse("Hello From Homepage of Product")
def add_product(request):
    print("Method Name:",request.method)
    if request.method=="GET":
        print("In if GET section")
        return render(request,'productapp/store_product.html')
    else:
        name=request.POST['pname']
        amt=request.POST['price']
        qty=request.POST['qty']
        cat=request.POST['ctgy']
        is_avail=request.POST['avail']

        #print("Product Name:",name)
        #print("Product Amount:",amt)
        #print("Quantity:",qty)
        #print("Category :",cat)
        #print("Availability :",is_avail)
        #Validation

        #Insert record into table
        p=Product.objects.create(name=name,price=amt,qty=qty,cat=cat,is_available=is_avail)
        #print(p)
        p.save()
        return redirect('/productapp/productdash')

        return HttpResponse("Data Inserted")

def product_dashboard(request):
    context={}
    #fetch data from model or table
    p=Product.objects.all() #select * from productapp_product;
    '''print(p)
    print(p[0])
    print(p[1])
    print("Product Name:",p[0].name)
    print("Product Price:",p[0].price)
    print("Product Name:",p[1].name)
    print("Product Price:",p[1].price)
    print("Using dFor Loop")
    for x in p:
        print(x)
        print(x.name)
        print(x.price)
        print(x.is_available)'''
    context['product']=p
    return render(request,'productapp/dashboard.html',context)

def delete_product(request,pid):
    #fetch object to be deleted
    p=Product.objects.filter(id=pid)
    print("Object Deleted")
    #delete object
    p.delete()
    #redirect to dashboard
    return redirect('/productapp/productdash')

def update_product(request,pid):
    p=Product.objects.filter(id=pid)
    if request.method=="GET":
        #print(p)
        context={}
        context['product']=p
        #return HttpResponse("Data Fetched")
        return render(request,'productapp/editproduct.html',context)
    else:
        uname=request.POST['pname']
        uprice=request.POST['price']
        uqty=request.POST['qty']
        ucat=request.POST['ctgy']
        uavail=request.POST['avail']
        p.update(name=uname,price=uprice,qty=uqty,cat=ucat,is_available=uavail)
        return redirect("/productapp/productdash")


