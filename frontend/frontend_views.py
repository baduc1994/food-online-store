from django.shortcuts import redirect, render
from davur.models import *
from django.http import HttpResponse, JsonResponse
import json
from frontend.form import CustomerReviewForm, OrderForm, OrderOnlineForm, Productform, ReviewForm, ShippingForm
from users.forms import CustomUserForm, CustomerForm
from .models import *
from .urls import *
import random
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.core.paginator import Paginator

from django.utils import timezone



# For Customer

#Home page
def home_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    if request.user.is_authenticated:
        customer = request.user
        cart,created = CartOnline.objects.get_or_create(customer = customer)
        context= {
        'products':products,
        'categories':categories,
        'cart':cart
        }
        return render(request, 'frontend/home-page.html' ,context)
    else:
        context= {
            'products':products,
            'categories':categories,
        }
        return render(request, 'frontend/home-page.html' ,context)

# Register
def register_page(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontend:login-page')
    else:
        form = CustomerForm()
        context = {
            'form':form,
        }
        return render(request, 'frontend/register.html', context)

# Log in  
def login_page(request):
    if request.user.is_authenticated:
        return redirect('frontend:home-page')
    if request.method =='POST':
        email =request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email= email, password = password)
        if user is not None:
            login(request,user)
            return redirect('frontend:home-page')
        else: messages.info(request, 'User or password is not correct!')
    return render(request, 'frontend/login.html')

# Log out
def logout_page(request):
    logout(request)
    return redirect('frontend:home-page')

    
#Product-detail
def product_detail(request, id):
    product = Product.objects.get(id = id)
    reviews = Product_review.objects.filter(product = product).order_by('-time')
    paginator = Paginator(reviews, 5)
    page_numer = request.GET.get('page')
    reviews = paginator.get_page(page_numer)
    if request.user.is_authenticated:
        customer = request.user
        is_bought = ListOrderOnline.objects.filter(product_id = id, customer = customer).last()
        cart,created = CartOnline.objects.get_or_create(customer = customer)
        

        context = {
            'product':product,
            'cart':cart,
            'reviews':reviews,
            'is_bought':is_bought
            
        }
        return render(request, 'frontend/product-detail.html',context)

    context = {
        'product':product,
        'reviews':reviews,
    }
    return render(request, 'frontend/product-detail.html',context)

# Cart page
@login_required(login_url='frontend:login-page')
def cart_page(request):
    if request.user.is_authenticated:
        customer = request.user
        cart,created = CartOnline.objects.get_or_create(customer = customer)
        items = cart.cart.all()
        nullitems = cart.nullitem.all()
    else:
        items = []
    context = {
        'items':items,
        'cart':cart,
        'nullitems':nullitems
        
    }

    return render(request, 'frontend/cart-page.html', context)

# Add to cart online
@login_required(login_url='frontend:login-page')
def addtocart_online(request):
    if request.method == "POST":
        prod_id = int(request.POST['product_id'])
        prod_qty = int(request.POST['product_qty'])
        cart_id = int(request.POST['cart_id'])       
        product_check = Product.objects.get(id = prod_id)
        if (CartItemOnline.objects.filter(product_id = prod_id, cart_id = cart_id)):
            return JsonResponse({'status':"Product already in cart"})
        else:
            if product_check.product_qty >= prod_qty:      
                item = CartItemOnline.objects.create(product_id = prod_id, quantity = prod_qty, cart_id = cart_id)
                product_check.product_qty = product_check.product_qty - prod_qty
                product_check.save()
            elif 0 < product_check.product_qty < prod_qty:
                item2 = NullItemOnline.objects.create(product_id = prod_id, cart_id = cart_id,quantity = product_check.product_qty)
            else:
                item3 = NullItemOnline.objects.create(product_id = prod_id, cart_id = cart_id,quantity = 0)
    return redirect('frontend:table') 

#Update Cart
@login_required(login_url='frontend:login-page')
def updateCart_online(request):
    if request.method =="POST":
        prod_id = int(request.POST['product_id']) 
        prod_qty = int(request.POST['product_qty'])
        cart_id = int(request.POST['cart_id'])
        product_check = Product.objects.get(id = prod_id)

        if (CartItemOnline.objects.filter(product_id = prod_id, cart_id = cart_id)):
            item = CartItemOnline.objects.get(product_id = prod_id, cart_id = cart_id)

            if prod_qty > item.quantity:
                minus_qty = prod_qty - item.quantity

                if product_check.product_qty < minus_qty:
                    NullItemOnline.objects.create(product_id = prod_id, cart_id = cart_id,quantity = product_check.product_qty)

                elif product_check.product_qty == 0:
                    NullItemOnline.objects.create(product_id = prod_id, cart_id = cart_id,quantity = 0)
                else:    
                    product_check.product_qty = product_check.product_qty + item.quantity 
                    product_check.save()
                    item.quantity = prod_qty
                    item.save()
                    product_check.product_qty = product_check.product_qty - prod_qty
                    product_check.save()           
                    return JsonResponse({'status': "Update Successfully"})
            else:
                product_check.product_qty = product_check.product_qty + item.quantity 
                product_check.save()
                item.quantity = prod_qty
                item.save()
                product_check.product_qty = product_check.product_qty - prod_qty
                product_check.save()           
                return JsonResponse({'status': "Update Successfully"})

    return redirect('frontend:table')

# Delete Cart
@login_required(login_url='frontend:login-page')
def deleteCartItem_online(request):
    if request.method =="POST":
        prod_id = int(request.POST['product_id'])
        cart_id = int(request.POST['cart_id'])        
        product_check = Product.objects.get(id = prod_id)           
        if (CartItemOnline.objects.filter(product_id = prod_id, cart_id = cart_id)):
            item = CartItemOnline.objects.get(product_id = prod_id, cart_id = cart_id)
            product_check.product_qty = product_check.product_qty + item.quantity 
            product_check.save()
            item.delete()           
            return JsonResponse({'status': "Delete Successfully"})
    return redirect('frontend:table')


# Delete Null Item
@login_required(login_url='frontend:login-page')
def deleteNullItem_online(request):
    if request.method =="POST":        
        null_cart_id = int(request.POST['null_cart_id'])
        if (NullItemOnline.objects.filter(cart_id = null_cart_id)):
            item2 = NullItemOnline.objects.filter(cart_id = null_cart_id)
            item2.delete()           
            return JsonResponse({'status': "Delete Successfully"})
    return redirect('frontend:table') 


# Discount code
@login_required(login_url='frontend:login-page')
def discount_code(request):
    if request.method == "POST":

        code = request.POST['code']
        
        cart_id = request.POST['cart_id']
        discount_code = Discount.objects.get(code = code)
        discount_value = int(discount_code.value)
        cart = CartOnline.objects.get(id = cart_id)
        cart.discount = discount_value
        
        cart.save()
    return redirect('frontend:checkout-page')


# Checkout page
@login_required(login_url='frontend:login-page')
def checkout_page(request):
    if request.user.is_authenticated:
        customer = request.user
        if request.method =='POST':
            form = ShippingForm(request.POST)
            if form.is_valid():
                shipping, created = ShippingAddress.objects.get_or_create(customer = customer)

                shipping.address = form.cleaned_data['address']
                shipping.state = form.cleaned_data['state']
                shipping.city = form.cleaned_data['city']
                shipping.zip = form.cleaned_data['zip']
                shipping.mobile = form.cleaned_data['mobile']
                shipping.save()

                return redirect('frontend:purchase-page')
        else:
            form = ShippingForm()
        try:
            cart = CartOnline.objects.get(customer = customer)
            items = cart.cart.all()
            context = {
            'items':items,
            'cart':cart,
            'customer':customer
            }
            return render(request, 'frontend/checkout-page.html',context)
        except:
            return redirect('frontend:home-page')

# Purchase
@login_required(login_url='frontend:login-page')
def purchase_page(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = OrderOnlineForm(request.POST)
            if form.is_valid():
                customer = request.user
                try:
                    cart = CartOnline.objects.get(customer = customer)
                    items = cart.cart.all()
                    if items.count() == 0:
                        return redirect('frontend:home-page')
                    else:

                        randomID = ''
                        for i in range(5):
                            a = str(random.randint(0,9))
                            randomID += a 
                        randomID = '#' + randomID 
                        order = OrderOnline.objects.create(customer = customer)
                        order.payment_method = form.cleaned_data['payment_method'] 
                        order.order_id = randomID
                        order.total_item = cart.get_cart_items
                        order.total_price = cart.get_cart_total
                        order.discount = cart.discount

                        
                        order.save()

                        order_tracking = OrderTracking.objects.create(order = order)


                        for i in items:
                            pro_id = i.product.id
                            list_orders = ListOrderOnline.objects.create(product_id = pro_id, order = order,customer = customer)

                            # list_orders.product_name = i.product.product_name
                            # list_orders.product_price = i.product.product_price
                            list_orders.product_qty = i.quantity
                            list_orders.save()
                            


                        id = str(order.order_id)

                        
                        return redirect("frontend:thank-you", id)
                except:
                    return redirect('frontend:home-page')

        form = OrderOnlineForm()  
        context = {
            'form':form,
        }  

        return render(request, 'frontend/purchase-page.html',context)


# Thank you
@login_required(login_url='frontend:login-page')
def thankyou_page(request, id):
    if request.user.is_authenticated:
        customer = request.user
        customer.is_customer = True
        customer.save()
        order = OrderOnline.objects.get(customer = customer, order_id = id)
        # order.is_complete = True
        customer_history, created = CustomerHistory.objects.get_or_create(customer = customer)
        customer_history.buy_qty = customer_history.buy_qty + 1
        customer_history.total_spent += order.total_price
        customer_history.save()
        if customer_history.buy_qty > 1:
            order.is_return = True
            customer_history.last_order_date = order.created_at
        customer_history.save()
        order.save()
        
        
        cart = CartOnline.objects.get(customer = customer)
        cart.delete()  
        return render(request, 'frontend/thankyou-page.html')


# Customer Review
@login_required(login_url='frontend:login-page')
def customer_review(request,id):
    if request.user.is_authenticated:
        customer = request.user
        if request.method =='POST': 
            form = CustomerReviewForm(request.POST)
            if form.is_valid():
                review = Product_review.objects.create(customer=customer, product_id = id)
                review.review_content = form.cleaned_data['review_content']
                review.rating = form.cleaned_data['rating']
                review.save()
                return redirect('frontend:view-product', id)
                
        else:
            form = CustomerReviewForm()
            return render(request, 'frontend/customer-review.html',{'customer':customer, 'form':form})

# Order history
@login_required(login_url='frontend:login-page')
def order_history(request):
    if request.user.is_authenticated:
        customer1 = request.user
        if (OrderOnline.objects.filter(customer = customer1)):
            customer = CustomerHistory.objects.get(customer = customer1)
            orders = OrderOnline.objects.filter(customer = customer1)
            context = {
                'customer':customer,
                'orders': orders,
            }

            return render(request, 'frontend/order-history.html',context)
        
        return render(request, 'frontend/order-tracking.html')


# Tracking order
@login_required(login_url='frontend:login-page')
def tracking_order(request):
    if request.user.is_authenticated:
        customer = request.user
        if (OrderOnline.objects.filter(customer = customer)):
            new_order = OrderOnline.objects.filter(customer = customer).last()
            order_tracking = OrderTracking.objects.get(order = new_order)
            
            context = {
                'new_order':new_order,
                'order_tracking':order_tracking
            }
            return render(request, 'frontend/order-tracking.html',context)

        
        return render(request, 'frontend/order-tracking.html')
        







# For Store Owner

# Table
@login_required(login_url='davur:login')
def table(request):
    tables = Table.objects.all()
    context = {'tables': tables}
    return render(request, 'frontend/table.html', context)

# Cart
@login_required(login_url='davur:login')
def cart(request,id):
    products = Product.objects.all()
    table = Table.objects.get(id = id)
    categories = Category.objects.all()
    if table.available == True:
        table.available = False
        table.save()
        cart = Cart.objects.create(table = table)        
        context= {'products':products, 'table':table, 'cart':cart, 'categories':categories}
        return render(request, 'frontend/cart.html' ,context)
    else:
        cart = Cart.objects.get(table__id=id)
        items = cart.cartitem_set.all()
        nullitems = cart.nullitem_set.all()
        context= {'items': items, 'cart':cart,'products':products, 'nullitems': nullitems, 'categories':categories}
        return render(request, 'frontend/cart.html',context)
    
@login_required(login_url='davur:login')
def cart_demo(request,id):
    products = Product.objects.all()
    table = Table.objects.get(id = id)
    categories = Category.objects.all()
    if table.available == True:
        table.available = False
        table.save()
        cart = Cart.objects.create(table = table)        
        context= {'products':products, 'table':table, 'cart':cart, 'categories':categories}
        return render(request, 'frontend/cart.html' ,context)
    else:
        cart = Cart.objects.get(table__id=id)
        items = cart.cartitem_set.all()
        nullitems = cart.nullitem_set.all()
        context= {'items': items, 'cart':cart,'products':products, 'nullitems': nullitems, 'categories':categories}
        return render(request, 'frontend/cart-demo.html',context)

@login_required(login_url='davur:login')
def addtocart(request):
    if request.method == "POST":
        prod_id = int(request.POST['product_id'])
        prod_qty = int(request.POST['product_qty'])
        cart_id = int(request.POST['cart_id'])       
        product_check = Product.objects.get(id = prod_id)
        if (CartItem.objects.filter(product_id = prod_id, cart_id = cart_id)):
            return JsonResponse({'status':"Product already in cart"})
        else:
            if product_check.product_qty >= prod_qty:      
                item = CartItem.objects.create(product_id = prod_id, quantity = prod_qty, cart_id = cart_id)
                product_check.product_qty = product_check.product_qty - prod_qty
                product_check.save()
            elif 0 < product_check.product_qty < prod_qty:
                item2 = NullItem.objects.create(product_id = prod_id, cart_id = cart_id,quantity = product_check.product_qty)
            else:
                item3 = NullItem.objects.create(product_id = prod_id, cart_id = cart_id,quantity = 0)
    return redirect('frontend:table') 

#Update Cart
@login_required(login_url='davur:login')
def updateCart(request):
    if request.method =="POST":
        prod_id = int(request.POST['product_id']) 
        prod_qty = int(request.POST['product_qty'])
        cart_id = int(request.POST['cart_id'])
        product_check = Product.objects.get(id = prod_id)

        if (CartItem.objects.filter(product_id = prod_id, cart_id = cart_id)):
            item = CartItem.objects.get(product_id = prod_id, cart_id = cart_id)

            if prod_qty > item.quantity:
                minus_qty = prod_qty - item.quantity

                if product_check.product_qty < minus_qty:
                    NullItem.objects.create(product_id = prod_id, cart_id = cart_id,quantity = product_check.product_qty)

                elif product_check.product_qty == 0:
                    NullItem.objects.create(product_id = prod_id, cart_id = cart_id,quantity = 0)
                else:    
                    product_check.product_qty = product_check.product_qty + item.quantity 
                    product_check.save()
                    item.quantity = prod_qty
                    item.save()
                    product_check.product_qty = product_check.product_qty - prod_qty
                    product_check.save()           
                    return JsonResponse({'status': "Update Successfully"})
            else:
                product_check.product_qty = product_check.product_qty + item.quantity 
                product_check.save()
                item.quantity = prod_qty
                item.save()
                product_check.product_qty = product_check.product_qty - prod_qty
                product_check.save()           
                return JsonResponse({'status': "Update Successfully"})

    return redirect('frontend:table')

# Delete Cart
@login_required(login_url='davur:login')
def deleteCartItem(request):
    if request.method =="POST":
        prod_id = int(request.POST['product_id'])
        cart_id = int(request.POST['cart_id'])        
        product_check = Product.objects.get(id = prod_id)           
        if (CartItem.objects.filter(product_id = prod_id, cart_id = cart_id)):
            item = CartItem.objects.get(product_id = prod_id, cart_id = cart_id)
            product_check.product_qty = product_check.product_qty + item.quantity 
            product_check.save()
            item.delete()           
            return JsonResponse({'status': "Delete Successfully"})
    return redirect('frontend:table')


# Delete Null Item
@login_required(login_url='davur:login')
def deleteNullItem(request):
    if request.method =="POST":        
        null_cart_id = int(request.POST['null_cart_id'])
        if (NullItem.objects.filter(cart_id = null_cart_id)):
            item2 = NullItem.objects.filter(cart_id = null_cart_id)
            item2.delete()           
            return JsonResponse({'status': "Delete Successfully"})
    return redirect('frontend:table') 

# Checkout
@login_required(login_url='davur:login')
def checkout(request,id):

    if request.method =='POST': 
        form = OrderForm(request.POST)
        if form.is_valid():
            # b = DonHang.objects.last()                  
            randomID = ''
            for i in range(5):
                a = str(random.randint(0,9))
                randomID += a 
            # randomID = '#' + str(b.id) + randomID
            randomID = '#' + randomID 
            # today = timezone.now().date
            # filter_date, created = FilterDate.objects.get_or_create(filter_date = today)

            order = Order.objects.create(order_id = randomID)

            cart = Cart.objects.get(id=id)
            table = Table.objects.get(id = cart.table.id)
            table.available = True
            table.save()
            items = cart.cartitem_set.all()
            order.total_item = cart.get_cart_items
            order.total_price = cart.get_cart_total            
            order.customer_name = form.cleaned_data['customer_name']
            order.payment_method = form.cleaned_data['payment_method']
            order.discount = form.cleaned_data['discount']
            order.save()

            

            if order.discount == '10':
                order.total_price = order.discount10()       
            elif order.discount == '20':
                order.total_price = order.discount20()
            order.save()
            new_customer_name = form.cleaned_data['customer_name']
            all_name = Customer.objects.values_list('name', flat=True)
            if new_customer_name in all_name:
                customer_return = Customer.objects.get(name = new_customer_name)
                customer_return.buy_qty +=1
                customer_return.total_spent = customer_return.total_spent + order.total_price
                customer_return.last_order_date = order.created_at
                customer_return.save()

                order.is_return = True
                order.total_price = order.isreturn()
                order.save()
            else:
                new_customer = Customer.objects.create()
                new_customer.name = new_customer_name
                new_customer.total_spent = order.total_price
                # new_customer.join_date = new_customer.last_order_date
                new_customer.save()
                        
            for i in items:
                list_orders = ListOrder.objects.create(order = order)
                list_orders.product_name = i.product.product_name
                list_orders.product_price = i.product.product_price
                list_orders.product_qty = i.quantity
                list_orders.save()
            cart.delete()           
            pk = order.id
            return redirect('frontend:purchase', pk)
    else:
        form = OrderForm()           
        return render(request, 'frontend/checkout.html', {'form':form} )

#Purchase
@login_required(login_url='davur:login')
def purchase(request,pk):   
    confirm_order = Order.objects.get(id = pk)
    show_list_items = confirm_order.listorder_set.all()
    context = {
        'confirm_order':confirm_order,
        'show_list_items':show_list_items
    }    
    return render(request,'frontend/purchase.html', context)

# Success
@login_required(login_url='davur:login')
def success(request,id):
    success_order = Order.objects.get(id = id)
    success_order.is_complete = True
    success_order.save()
    a = success_order.customer_name
    customer_name = Customer.objects.get(name = a)
    
    return render(request, 'frontend/success.html', {'customer_name':customer_name})

#Review
@login_required(login_url='davur:login')
def review(request,id):
    customer = Customer.objects.get(id = id)
    if request.method =='POST': 
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Restaurant_review.objects.create(customer_id = id)
            review.review_content = form.cleaned_data['review_content']
            review.rating = form.cleaned_data['rating']
            review.save()
            return redirect('frontend:thankyou')
            
    else:
        form = ReviewForm()
        return render(request, 'frontend/review.html',{'customer':customer, 'form':form})


# Thank you
@login_required(login_url='davur:login')
def thankyou(request):
    return render(request, 'frontend/thankyou.html')       
        
    

# Search
@login_required(login_url='davur:login')
def search(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        searched = request.POST['searched']
        
        if searched:
            no_search = 'show'
        else:
            # no_search = 'hidden'
            cart_id = int(request.POST['id_cart'])
            cart = Cart.objects.get(id = cart_id)
            table_id = cart.table.id
            return redirect('frontend:cart',table_id)
            
        keys = Product.objects.filter(product_name__contains = searched)
        if keys:
            found = "show"
            not_found = "hidden"
        else:
            found = "hidden"
            not_found = "show"
        cart_id = int(request.POST['id_cart']) # id cua cart hien tai
        cart = Cart.objects.get(id = cart_id)
        nullitems = cart.nullitem_set.all()
        items = cart.cartitem_set.all()
        context = {
            'searched': searched,
            'keys':keys,
            'found':found,
            'not_found':not_found,
            'categories':categories,
            'no_search': no_search,
            'items': items,
            'cart':cart,
            'nullitems':nullitems
        }
        return render(request, 'frontend/search.html', context)
    # else:
    #     return redirect('frontend:search')


# Category
@login_required(login_url='davur:login')
def category(request, slug, id):
    categories = Category.objects.all()
    products = Product.objects.filter(category__slug = slug)

    active_category = Category.objects.get(slug = slug)
    
    cart = Cart.objects.get(id = id)
    nullitems = cart.nullitem_set.all()
    table_id = cart.table.id
    items = cart.cartitem_set.all()

    context = {
        
        'categories':categories,
        'items': items,
        'cart':cart,
        'products': products,
        'table_id':table_id,
        'nullitems':nullitems,
        'active_category':active_category

    }
    return render(request, 'frontend/order-category.html', context)




def front_authentication(request):
    return render(request, 'frontend/front-authentication.html')


def front_people(request):
    return render(request, 'frontend/front-people.html')


# Upload Item
@login_required(login_url='davur:login')
@permission_required({'users.view_customuser'}, raise_exception=True)
def front_upload_item(request):
    if request.method == 'POST':
        form = Productform(request.POST, request.FILES)
        if form.is_valid():
            randomID = ''
            for i in range(5):
                a = str(random.randint(0,9))
                randomID += a 
            randomID = '#' + randomID

            form.save()
            new_product = Product.objects.last()
            new_product.product_code = randomID
            new_product.save()
        return redirect('frontend:front-upload-item')       
    else:
        form = Productform()
        context = {'form': form}
        return render(request, 'frontend/front-upload-item.html', context)


def front_login(request):
    return render(request, 'frontend/front-login.html')


def page_register(request):
    return render(request, 'frontend/page-register.html')


# Demo charjs
def chartJs(request):

    # pro_name = Product.objects.values_list('product_name', flat=True)
    # pro_buy = Product.objects.values_list('buy_qty', flat=True)

    
    main_cate = Product.objects.filter(category__name = 'Main')

    return_customers = Customer.objects.filter(buy_qty__gt = 1).count()
    new_customers = Customer.objects.filter(buy_qty = 1).count()

    context = {
        
        'main_cate':main_cate,
        'return_customers':return_customers,
        'new_customers':new_customers

    }
    return render(request, 'frontend/chart.html',context)

