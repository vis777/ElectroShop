from django.shortcuts import render,redirect
from Mainapp.models import CategoryDb,ProductDb
from Frontapp.models import ContactDb,RegisterDb,CartDb
from django.contrib import messages
# Create your views here.
def homepage(request):
    cat = CategoryDb.objects.all()
    return render(request,"Home.html", {'cat':cat})
def productspage(request):
    pro = ProductDb.objects.all()
    return render(request,"Products.html",{'pro':pro})
def product_filter_page(request, cat_name):
    data = ProductDb.objects.filter(Product_Category=cat_name)
    return render(request, "Products_Filtered.html", {'data':data})
def singleproductpage(request, proid):
    data = ProductDb.objects.get(id=proid)
    return render(request, "SingleProduct.html", {'data':data})
def contactpage(request):
    return render(request, "Contact.html")
def aboutpage(request):
    return render(request, "AboutUs.html")
def servicepage(request):
    return render(request, "Services.html")
def savecontact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        mes = request.POST.get('message')
        obj = ContactDb(Contact_Name=na, Contact_Email=em, Subject=sub, Message=mes)
        obj.save()
        return redirect(contactpage)
def user_login(request):
    return render(request,"Register.html")
def savereg(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        eml = request.POST.get('email')
        use = request.POST.get('username')
        pas = request.POST.get('password')
        obj = RegisterDb(Name=na, Mobile_Number=mob, Email=eml ,UserName=use, PassWord=pas)
        obj.save()
        return redirect(user_login)
def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')
        if RegisterDb.objects.filter(UserName=un,PassWord=pwd).exists():
            request.session['UserName']=un
            request.session['PassWord']=pwd
            messages.success(request, "welcome")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect(user_login)
    return redirect(user_login)
def user_logout(request):
    del request.session['UserName']
    return redirect(user_login)
def cartpage(request):
    data = CartDb.objects.filter(Username=request.session['UserName'])
    total_price = 0
    for i in data:
        total_price = total_price+i.Total_Price
    return render(request,"Cart.html" , {'data':data, 'total_price':total_price})
def savecart(request):
    if request.method == "POST":
        na = request.POST.get('username')
        pna = request.POST.get('productname')
        qty = request.POST.get('quantity')
        tp = request.POST.get('total')
        des = request.POST.get('description')
        obj = CartDb(Username = na, Productname = pna, Quantity = qty, Total_Price = tp, Description = des)
        obj.save()
        return redirect(cartpage)
def deletecart(request, dataid):
    cart = CartDb.objects.filter(id=dataid)
    cart.delete()
    return redirect(cartpage)
def checkoutpage(request):
    return render(request, "Checkout.html")