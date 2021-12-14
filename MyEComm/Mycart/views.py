from django.shortcuts import render
from django.http import HttpResponse
from .models import Mycart,Contact,Order,OrderTracker
from math import ceil, pi
import json

# Create your views here.
def index(request):
    allProds = []
    # catprods = Mycart.objects.values('category', 'id')
    # fprod = Mycart.objects.values('id')
    # print(len(fprod))
    # for i in range(1,4):
    # f_prod = Mycart.objects.values(id)
    #     print(f_prod)
    # f_prod = []
    # all_fprod = {f_prod[Mycart.objects.filter(id=i)] for i in range(1,4)}
    # print(all_fprod)
    # cats = {item['category'] for item in catprods}
    for cat in range(1,4):
        prod = Mycart.objects.filter(id=cat)
        n = len(prod)
        # nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, 4)])
        params = {'allProds':allProds}
    return render(request, 'Mycart/backup1.html', params)

def CategoryItem(request,mycat):
    AllProducts = []
    allcat = {1:'Electronics',2:'Home product',3:'Computer',4:'Bag',5:'phone',6:'Footwear',7:'health and beauty',8:'Jewellery',9:'Baby Products',10:'Sports & Fitness',11:'',12:'Beauty & Luxury beauty',13:'TVs & Appliances',14:'Women Fashion',15:'Men Fashion',16:'Kid Fashion',17:'Grocery & Gourment',18:'Daily essentials'}
    page_cat = allcat[mycat]
    allcatitems = Mycart.objects.filter(category = page_cat) 
    total_items = len(allcatitems)
    AllProducts.append([allcatitems,total_items])
    ProductList = {'AllProducts':AllProducts}
    # AllCatProds = Mycart.objects.values('category','id').filter(category = page_cat)
    # listItems = {item['id'] for item in AllCatProds}
    # print(listItems)
    # print(total_items)
    # for i in range(total_items):
        # print(allcatitems[i])
    # print(cat_products)
    # cat_params = {'cat_products':cat_products}
    return render(request,'Mycart/CategoryItem.html',ProductList)

def about(request):
    return render(request,'Mycart/about.html')

def contact(request):
    if request.method =="POST":
        name= request.POST.get('name','')
        email = request.POST.get('email','')
        message = request.POST.get('message','')
        print(name,email,message)
        cn1=Contact(name=name,email=email,message=message)
        cn1.save()
    return render(request,'Mycart/contact.html')

def tracker(request):
    if request.method =="POST":
        orderid= request.POST.get('orderid','')
        email = request.POST.get('email','')
        try:
            order = Order.objects.filter(order_id=orderid,email = email)
            if(len(order))>0:
                update = OrderTracker.objects.filter(order_id=orderid)
                Track_details = []
                for item in update:
                    Track_details.append({'Track_desc': item.Track_desc,'time':item.Track_time})
                    Track_response = json.dumps(Track_details)
                    return HttpResponse(Track_response)
            else:
                pass
        except Exception as e:
            pass    
    return render(request,'Mycart/tracker.html')
    
def search(request):
    return render(request,'Mycart/search.html')
    
def productview(request,myid):
    prodlist = []
    # Featch the product using id
    product = Mycart.objects.filter(id=myid)
    prodcat = Mycart.objects.filter(id=myid).values('category')
    item = product[0]
    cat = prodcat[0]['category']
    prodlist.append([item,cat])
    prodview = {'prodview': prodlist}
    # print(prodlist[0])

    return render(request,'Mycart/productview1.html',{'product': item})
    
def checkout(request):
    if request.method =="POST":
        name= request.POST.get('name','')
        order_json = request.POST.get('order_json','')
        mobile = request.POST.get('mobile','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        pincode = request.POST.get('pin','')
        city = request.POST.get('city','')
        zip = request.POST.get('zip','')
        landmark = request.POST.get('landmark','')
        state = request.POST.get('state','')
        order=Order(name=name,mobile=mobile,email=email,address=address,pincode=pincode,city=city,zip=zip,landmark=landmark,state=state,order_json=order_json)
        order.save()
        id = order.order_id
        tracker = OrderTracker(order_id = order.order_id,Track_desc = "Order placed")
        tracker.save()
    return render(request,'Mycart/checkout.html')
    

