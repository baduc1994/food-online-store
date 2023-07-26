from django.urls import path
from davur import davur_views
from users import users_views

app_name = 'davur'
urlpatterns = [

    path('users/', users_views.users, name="users"),
    path('user-details/<int:id>/', users_views.user_details, name="user-details"),
    path('add-user/', users_views.add_user, name="add-user"),
    path('edit-user/<int:id>/', users_views.edit_user, name="edit-user"),
    path('delete-user/<int:id>/', users_views.delete_user, name="delete-user"),
    path('delete-multiple-user/', users_views.delete_multiple_user, name="delete-multiple-user"),

    path('login/', users_views.login_user, name="login"),
    path('logout/', users_views.logout_user, name="logout"),

    path('group-edit/<int:id>/', users_views.group_edit, name="group-edit"),
    path('group-delete/<int:id>/', users_views.group_delete, name="group-delete"),
    path('group-add/', users_views.group_add, name="group-add"),

    path('edit-permissions/<int:id>/', users_views.edit_permissions, name="edit-permissions"),
    path('delete-permissions/<int:id>/', users_views.delete_permissions, name="delete-permissions"),
    path('assign-permissions-to-user/<int:id>/', users_views.assign_permissions_to_user,
         name="assign-permissions-to-user"),
    path('signup/', users_views.signup, name="signup"),
    path('activate/<uidb64>/<token>/', users_views.activate, name='activate'),

    path('', davur_views.index, name="index"),
    path('dashboard/', davur_views.dashboard, name="dashboard"),
    path('page-analytics/', davur_views.page_analytics, name="page-analytics"),
    path('page-review/', davur_views.page_review, name="page-review"),
    path('page-review/<int:id>', davur_views.filter_review, name="filter-review"),
    path('page-general-customers/', davur_views.page_general_customers, name="page-general-customers"),
    path('page-general-customers/<str:a>', davur_views.filter_customers, name="filter-customers"),
    path('customer-detail/<int:id>', davur_views.customer_detail, name="customer-detail"),
    path('delete-customer/<int:id>', davur_views.delete_customer, name="delete-customer"),
    
    path('online-customers/', davur_views.online_customers, name="online-customers"),


    path('ecom-product-list/', davur_views.ecom_product_list, name="ecom-product-list"),
    path('product-detail/<int:id>', davur_views.product_detail, name="product-detail"),
    path('delete-product/<int:id>', davur_views.delete_product, name="delete-product"),

    # create filter by categories
    path('category/<str:slug>', davur_views.filter_by_categories, name="filter-by-categories"),

    path('ecom-product-order/', davur_views.ecom_product_order, name="ecom-product-order"),

    path('order-status/', davur_views.order_status, name="order-status"),
    path('update-status/<int:id>/<str:status>', davur_views.update_status, name="update-status"),
    
    path('detail-order/<int:id>', davur_views.detail_order, name="detail-order"),

    path('delete-order/<int:id>', davur_views.delete_order, name="delete-order"),

    
    
    

    # demo
    path('demo/', davur_views.revenue, name="revenue"),


]
