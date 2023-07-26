from django.urls import path
from frontend import frontend_views

app_name = 'frontend'
urlpatterns = [

    # For customer
    path('', frontend_views.home_page, name="home-page"),
    path('sign-up/', frontend_views.register_page, name="register"),
    path('login/', frontend_views.login_page, name="login-page"),
    path('logout/', frontend_views.logout_page, name="logout-page"),

    path('product/<int:id>', frontend_views.product_detail, name="view-product"),
    path('cart/', frontend_views.cart_page, name="cart-page"),
    path('addtocart-onl/', frontend_views.addtocart_online, name="addtocart-online"),
    path('updatecart-onl/', frontend_views.updateCart_online, name ='updatecart-online'),
    path('delete-cart-item-onl/', frontend_views.deleteCartItem_online, name ='delete-cart-item-online'),
    path('delete-null-item-onl/', frontend_views.deleteNullItem_online, name ='delete-null-item-online'),
    path('discount-code/', frontend_views.discount_code, name ='discount-code'),
    
    path('checkout/', frontend_views.checkout_page, name="checkout-page"),
    path('purchase/', frontend_views.purchase_page, name="purchase-page"),
    path('thank-you/<str:id>', frontend_views.thankyou_page, name="thank-you"),

    path('customer_review/<int:id>', frontend_views.customer_review, name ='customer-review'),

    path('order-history/', frontend_views.order_history, name ='order-history'),
    path('tracking-order/', frontend_views.tracking_order, name ='tracking-order'),



    #For store owner

    path('front-authentication/', frontend_views.front_authentication, name="front-authentication"),
    # path('front-people/', frontend_views.front_people, name="front-people"),
    path('front-upload-item/', frontend_views.front_upload_item, name="front-upload-item"),
    # path('front-login/', frontend_views.front_login, name="front-login"),
    path('page-register/', frontend_views.page_register, name="page-register"),
    # path('update_item/', frontend_views.updateItem, name='update-item'),
    path('search/', frontend_views.search, name="search"),
    path('category/<str:slug>/<int:id>', frontend_views.category, name="category"),
    path('table/', frontend_views.table, name = 'table'),
    path('cart/<int:id>', frontend_views.cart, name = 'cart'),
    path('cart-demo/<int:id>', frontend_views.cart_demo, name = 'cart-demo'),
    path('checkout/<int:id>', frontend_views.checkout, name = 'checkout'),
    path('purchase/<pk>', frontend_views.purchase, name = 'purchase'),
    path('success/<int:id>', frontend_views.success, name = 'success'),
    path('addtocart/',frontend_views.addtocart, name='addtocart'),
    path('updatecart/', frontend_views.updateCart, name ='updatecart'),
    path('delete-cart-item/', frontend_views.deleteCartItem, name ='delete-cart-item'),
    path('delete-null-item/', frontend_views.deleteNullItem, name ='delete-null-item'),
    path('chartjs/', frontend_views.chartJs, name ='chart'),
    path('review/<int:id>', frontend_views.review, name ='review'),
    path('thankyou/', frontend_views.thankyou, name ='thankyou'),

    
    

]
