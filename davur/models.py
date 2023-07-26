from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


# For Store Owner

#Tabel
class Table(models.Model):
    name_table = models.CharField(max_length=50, blank=False, null=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name_table)

#Customer
class Customer(models.Model):
    name = models.CharField(max_length=100,null=True)
    buy_qty = models.IntegerField(default=1)
    join_date = models.DateTimeField(auto_now_add=True)
    total_spent = models.FloatField(default=0)
    last_order_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

#Category
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    slug = models.SlugField(max_length=100, blank=False, null=True, default=None)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# Product
class Product(models.Model):
    product_name = models.CharField(max_length=255, blank=False, null=False)
    product_price = models.FloatField(blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    product_qty = models.IntegerField()
    product_code = models.CharField(max_length=20, blank=False, null=True)
    product_image = models.ImageField(upload_to="product_images", blank=False, null=False)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    buy_qty = models.IntegerField(default=0)

    def revenue(self):
        return self.product_price * self.buy_qty

    @property
    def ImageURL(self):
        try:
            url = self.product_image.url
        except:
            url=""
        return url

    def __str__(self):
        return self.product_name
    
    @property
    def rating(self):
        reviews = self.review.all()
        count = len(reviews)
        if count == 0:
            return 0
        else:
            sum = 0
            for review in reviews:
                sum = sum + int(review.rating)
            return round(sum/count,1)

#Produc Review
class Product_review(models.Model):
    product = models.ForeignKey(Product, related_name='review', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review_content = models.TextField(blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=True)

    

    def __str__(self):
        return f"{self.customer}: {self.rating}"

# Restaurant Review    
class Restaurant_review(models.Model):
    # ratingChoices = (
    #     (1, '1'), 
    #     (2, '2'), 
    #     (3, '3'), 
    #     (4, '4'), 
    #     (5, '5')
    # )

    # rating = models.IntegerField(choices=ratingChoices, blank=False, null=False, default=5)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=False)
    review_content = models.TextField(blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def avg(self):
        if (Restaurant_review.objects.all()):
            count = Restaurant_review.objects.count()
            sum = 0
            all_reviews = Restaurant_review.objects.all()
            for review in all_reviews:
                sum = sum + int(review.rating)
            return round(sum/count,1)


    def __str__(self):
        return f"{self.customer}: {self.rating}"
    
 

 # Cart Model

# Cart   
class Cart(models.Model):
    table = models.OneToOneField(Table, on_delete=models.CASCADE, null=True, blank=False)     

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_items(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.quantity for item in cartitems])
        return total
    
    @property
    def get_cart_total(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.get_total for item in cartitems])
        return total

# Cart item model
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    
    @property
    def get_total(self):
        total = self.product.product_price * self.quantity
        return total

class NullItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)



# Date of order
class FilterDate(models.Model):
    filter_date = models.DateField(default=None)

   




# Order
class Order(models.Model):
    customer_name = models.CharField(max_length=100, blank=True, null= True)
    order_id = models.CharField(max_length=20, blank=False, null=True)    
    payment_method = models.CharField(max_length=20, blank=False, null=False)   
    discount = models.CharField(max_length=20, blank=False, null=False)
    total_item = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)
    is_return = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    filter_date = models.ForeignKey(FilterDate, related_name='filterdate', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def isreturn(self):       
        self.total_price = self.total_price * 0.9
        return round(self.total_price, 2)

    def discount10(self):
        self.total_price = self.total_price * 0.9
        return round(self.total_price, 2)

    def discount20(self):
        self.total_price = self.total_price * 0.8
        return round(self.total_price, 2)
    
    def __str__(self):
        return self.order_id
    
class ListOrder(models.Model):
    product_name = models.CharField(max_length=100,null=True)
    product_price = models.FloatField(default=0)
    product_qty = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=True)





# For Online Customer




# Cutomer history 
class CustomerHistory(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=True)
    buy_qty = models.IntegerField(default=0)
    join_date = models.DateTimeField(auto_now_add=True)
    total_spent = models.FloatField(default=0)
    last_order_date = models.DateTimeField(null=True)

    # def __str__(self):
    #     return self.customer
    
# Shipping address
class ShippingAddress(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip = models.IntegerField(null=True)
    mobile = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

# Discount code
class Discount(models.Model):
    code = models.CharField(max_length=20, null=True)
    value = models.IntegerField()

    def __str__(self):
        return self.code

# Customer Cart   
class CartOnline(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=True)
    discount = models.FloatField(default=0)
    

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_items(self):
        cartitems = self.cart.all()
        total = sum([item.quantity for item in cartitems])
        return total
    
    @property
    def get_cart_total(self):
        cartitems = self.cart.all()
        total = sum([item.get_total for item in cartitems])
        total = total - total * self.discount / 100
        return total
    @property
    def get_discount_price(self):
        cartitems = self.cart.all()
        total = sum([item.get_total for item in cartitems])
        total = total * self.discount / 100
        return total
    
    
    
    


# Customer Cart item
class CartItemOnline(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(CartOnline, related_name='cart', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    
    @property
    def get_total(self):
        total = self.product.product_price * self.quantity
        return total
    
# Null Item
class NullItemOnline(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(CartOnline, related_name='nullitem', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)


# Order
class OrderOnline(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=True)
    order_id = models.CharField(max_length=20, blank=False, null=True)    
    payment_method = models.CharField(max_length=20, blank=False, null=False)   
    discount = models.CharField(max_length=20, blank=False, null=False)
    total_item = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)
    is_return = models.BooleanField(default=False)
    statusChoices = (
        ('Order Placed', 'Order Placed'), 
        ('Packed', 'Packed'),
        ('In Transit', 'In Transit'), 
        ('Delivered', 'Delivered'), 
        ('Completed', 'Completed')
        
    )

    order_status = models.CharField(max_length=50, choices=statusChoices, null=True, default='Order Placed')
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id
    
# Order Tracking
class OrderTracking(models.Model):
    order = models.OneToOneField(OrderOnline, on_delete=models.CASCADE, blank=False, null=True)
    time_placed = models.DateTimeField(auto_now_add=True)
    time_packed = models.DateTimeField(null=True)
    time_transit = models.DateTimeField(null=True)
    time_delivery = models.DateTimeField(null=True)
    



# List Order Item
class ListOrderOnline(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    # product_name = models.CharField(max_length=100,null=True)
    # product_price = models.FloatField(default=0)
    product_qty = models.IntegerField(default=0)
    order = models.ForeignKey(OrderOnline, related_name='order', on_delete=models.CASCADE, blank=False, null=True)


    

    





            
