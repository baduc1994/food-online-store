from django.utils import timezone
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from django.db.models import *
from django.core.paginator import Paginator


from datetime import datetime


@login_required(login_url='davur:login')
def index(request):

    categories = Category.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 15)
    page_numer = request.GET.get('page')
    products = paginator.get_page(page_numer)
   

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'davur/shop/ecom-product-list.html', context)


@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def dashboard(request):
    revenue_total = Order.objects.aggregate(Sum('total_price')) # return a dic() {'total_price__sum':92456 }
    revenue_total = revenue_total.get('total_price__sum') # a number get method to get value in dic() by key
    revenue_total = round(revenue_total,2)
    total_customers = Customer.objects.count()
    return_customers = Customer.objects.filter(buy_qty__gt = 1).count()
    new_customers = Customer.objects.filter(buy_qty = 1).count()

    total_items = ListOrder.objects.count()
    total_order = Order.objects.count()

    # Revenur Chart
    total = FilterDate.objects.all().count()
    this_week = FilterDate.objects.all()[total - 7:]
    last_week = FilterDate.objects.all()[total-14:total-7]

    today = timezone.now().day
    this_month = FilterDate.objects.all()[total - today:]

    order_number = []
    revenue_this_week = []
    revenue_last_week = []


    for a in this_month:
        count = a.filterdate.all().count()
        order_number.append(int(count))

        

    for i in this_week:
        # count = i.filterdate.all().count()
        # order_number.append(int(count))

        orders = Order.objects.filter(filter_date = i)
        sum1 = 0
        for order in orders:
            sum1 = sum1 + order.total_price
        revenue_this_week.append(round(sum1,2))

    for j in last_week:
        orders = Order.objects.filter(filter_date = j)
        sum2 = 0
        for order in orders:
            sum2 = sum2 + order.total_price
        revenue_last_week.append(round(sum2,2))
            
    total_this_week = round(sum(revenue_this_week),2)
    total_last_week = round(sum(revenue_last_week),2)
    total_orders = sum(order_number)





    context = {
        'total_order': total_order,
        'revenue_total':revenue_total,
        'total_items':total_items,
        'total_customers':total_customers,
        'return_customers': return_customers,
        'new_customers':new_customers,
        'this_week':this_week,
        'order_number':order_number,
        'revenue_this_week':revenue_this_week,
        'revenue_last_week':revenue_last_week,
        'total_this_week':total_this_week,
        'total_last_week':total_last_week,
        'this_month':this_month,
        'total_orders':total_orders
    }
    return render(request, 'davur/index.html',context)


@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def page_analytics(request):
    products = Product.objects.all().order_by('-buy_qty')
    products = products[:10]
    bs_products = Product.objects.all()
    
    
   
    context ={
        'products':products,
        'bs_products':bs_products

    }
    return render(request, 'davur/page-analytics.html',context)



#Order Status
@login_required(login_url='davur:login')
def order_status(request):
    
    orders = OrderOnline.objects.all().order_by('-id')
    paginator = Paginator(orders, 10)
    page_numer = request.GET.get('page')
    orders = paginator.get_page(page_numer)
    status_list = ['Order Placed','Packed','In Transit', 'Delivered', 'Completed']
    context = {
        'orders':orders,
        'status_list':status_list
        
    }
    return render(request, 'davur/shop/order-status.html', context)

# Update status
@login_required(login_url='davur:login')
def update_status(request, id, status):
    order = OrderOnline.objects.get(id = id)
    order_tracking = OrderTracking.objects.get(order = order)
    order.order_status = status
    order.save()
    if status == 'Packed':
        order_tracking.time_packed = timezone.now()
    elif status == 'In Transit':
        order_tracking.time_transit = timezone.now()
    elif status == 'Delivered':
        order_tracking.time_delivery = timezone.now()
    order_tracking.save()


    return redirect("davur:order-status")


    
    

# Online Customer Page
def online_customers(request):
    pass

# Restaurant review
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def page_review(request):

    if (Restaurant_review.objects.all()):
        
        restaurant_reviews = Restaurant_review.objects.all().order_by('-id')
        paginator = Paginator(restaurant_reviews, 5)
        page_numer = request.GET.get('page')
        restaurant_reviews = paginator.get_page(page_numer)
        a = Restaurant_review.objects.last()
        avg = a.avg()
        context = {
            "restaurant_reviews": restaurant_reviews,
            'avg':avg
            
        }

        return render(request, 'davur/page-review.html', context)
    else:
        return redirect('davur:index')

# Filter review
# def filter_review(request):
    
    if request.method == 'POST':
        filter_rating = request.POST['filter-rating']
        if filter_rating =='all':
            return redirect('davur:page-review')
        else:
            rating_core = Restaurant_review.objects.filter(rating = filter_rating).order_by('-id')
            paginator = Paginator(rating_core, 5)
            page_numer = request.GET.get('page')
            rating_core = paginator.get_page(page_numer)
            a = Restaurant_review.objects.last()
            avg = a.avg()
           
            context = {
                'rating_core':rating_core,
                'avg':avg,
            }
            return render(request, 'davur/filter-review.html', context)
    else:
        return render(request, 'davur/filter-review.html')


# Filter review 
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def filter_review(request,id):
           
    rating_core = Restaurant_review.objects.filter(rating = id).order_by('-id')
    paginator = Paginator(rating_core, 5)
    page_numer = request.GET.get('page')
    rating_core = paginator.get_page(page_numer)
    a = Restaurant_review.objects.last()
    avg = a.avg()
    
    context = {
        'rating_core':rating_core,
        'avg':avg,
    }
    return render(request, 'davur/filter-review.html', context)
    

# Customer Lists
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def page_general_customers(request):
    customers = Customer.objects.all().order_by('-id')
    paginator = Paginator(customers, 15)
    page_numer = request.GET.get('page')
    customers = paginator.get_page(page_numer)
    context = {
        'customers': customers
    }
    return render(request, 'davur/page-general-customers.html', context)


# Filter Customer
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def filter_customers(request, a):
    if a =='total_spent':
        customers = Customer.objects.all().order_by('-total_spent') 
    elif a == 'buy_quantity':
        customers = Customer.objects.all().order_by('-buy_qty')
    paginator = Paginator(customers, 15)
    page_numer = request.GET.get('page')
    customers = paginator.get_page(page_numer)
    
    context = {
        'customers':customers,
        'a':a
    }
    return render(request, 'davur/filter-customers.html', context)
 
# Detail Customer
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def customer_detail(request, id):
    customer = Customer.objects.get(id = id)
    orders = Order.objects.filter(customer_name = customer.name) 
    context = {
        'customer':customer,
        'orders': orders,
    }
    return render(request, 'davur/customer-detail.html', context)


# Delete Customer
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def delete_customer(request, id):
    if(Customer.objects.get(id = id)):
        customer = Customer.objects.get(id = id)
        customer.delete()
        return redirect('davur:page-general-customers')
    else:
        return redirect('davur:page-general-customers')
    

# Product List
@login_required(login_url='davur:login')
def ecom_product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 15)
    page_numer = request.GET.get('page')
    products = paginator.get_page(page_numer)
   

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'davur/shop/ecom-product-list.html', context)

# Product detail
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def product_detail(request, id):
    product = Product.objects.get(id = id)
    return render(request, 'davur/shop/product-detail.html',{'product':product})


# Delete product
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def delete_product(request, id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect('davur:ecom-product-list')


# Create filter
@login_required(login_url='davur:login')
def filter_by_categories(request, slug):
    if(Category.objects.filter(slug = slug)):
        products = Product.objects.filter(category__slug=slug)
        categories = Category.objects.all()
        active_categoty = Category.objects.get(slug = slug)
        paginator = Paginator(products, 15)
        page_numer = request.GET.get('page')
        products = paginator.get_page(page_numer)
        context = {
            'products': products,
            'categories': categories,
            'active_categoty':active_categoty
            }
        return render(request, 'davur/shop/product-list-by-categories.html', context)

# Order List
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def ecom_product_order(request):
    orders = Order.objects.all().order_by('-id')
    paginator = Paginator(orders, 20)
    page_numer = request.GET.get('page')
    orders = paginator.get_page(page_numer)
    
    context = {
        'orders':orders,
    }
    return render(request, 'davur/shop/ecom-product-order.html', context)

# Detail Order
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def detail_order(request, id):
    
    order = Order.objects.get(id = id)
    list_items = order.listorder_set.all()

    context = {
        'order':order,
        'list_items':list_items
    }
    return render(request, 'davur/shop/detail-order.html',context)

# Delete Order 
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def delete_order(request, id):
    if (Order.objects.get(id = id)):
        order = Order.objects.get(id = id)
        order.delete()
        return redirect("davur:ecom-product-order")




# Dashboard
@login_required(login_url='davur:login')
def revenue(request):
    # revenue_total = Order.objects.values_list('total_price', flat=True)
    revenue_total = Order.objects.aggregate(Sum('total_price')) # return a dic()
    revenue_total = revenue_total.get('total_price__sum') # a number

    total_order = Order.objects.count()

    total_items = ListOrder.objects.count()

    total_customers = Customer.objects.count()
    return_customers = Customer.objects.filter(buy_qty__gt = 1).count()
    new_customers = Customer.objects.filter(buy_qty = 1).count()

    # most_selling_pro = Product.objects.all().aggregate(Max('buy_qty'))
    # most_selling_pro = most_selling_pro.get('buy_qty__max')

    most_selling_pro = Product.objects.order_by('-buy_qty')


    # revenue
    # revenue_this_weeks = Order.objects.all().order_by('-set_time')[:7]
    # revenue_last_weeks = Order.objects.all().order_by('-set_time')[7:14]

    # order qty
    total = FilterDate.objects.all().count()
    this_week = FilterDate.objects.all()[total - 7:]
    last_week = FilterDate.objects.all()[total-14:total-7]
    order_number = []
    revenue_this_week = []
    revenue_last_week = []

    for i in this_week:
        count = i.filterdate.all().count()
        order_number.append(int(count))

        orders = Order.objects.filter(filter_date = i)
        sum1 = 0
        for order in orders:
            sum1 = sum1 + order.total_price
        revenue_this_week.append(round(sum1,2))

    for j in last_week:
        orders = Order.objects.filter(filter_date = j)
        sum2 = 0
        for order in orders:
            sum2 = sum2 + order.total_price
        revenue_last_week.append(round(sum2,2))
            
    total_this_week = round(sum(revenue_this_week),2)
    total_last_week = round(sum(revenue_last_week),2)
    
    
    # day = timezone.now().day
    # month = timezone.now().month
    # year = timezone.now().year

    context = {
     
        'this_week':this_week,
        'order_number':order_number,
        'revenue_this_week':revenue_this_week,
        'revenue_last_week':revenue_last_week,
        'total_this_week':total_this_week,
        'total_last_week':total_last_week,
       


     
        
        

        

    }
    return render(request, 'davur/shop/demo.html', context)
