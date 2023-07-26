from django import forms
from davur.models import OrderOnline, Product, Order, Restaurant_review, ShippingAddress, Product_review

class Productform(forms.ModelForm):
    
    class Meta:
        model = Product

        fields = ['product_name', 'product_price', 'product_qty', 'description','product_image','category']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_name','payment_method','discount')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Restaurant_review
        fields = ('review_content','rating')

class CustomerReviewForm(forms.ModelForm):
    class Meta:
        model = Product_review
        fields = ('review_content','rating')

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('address','state', 'city', 'zip', 'mobile')

class OrderOnlineForm(forms.ModelForm):
    class Meta:
        model = OrderOnline
        fields = ('payment_method',)

    




