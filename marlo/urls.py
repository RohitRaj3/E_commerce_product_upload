
from django.urls import path
from marlo import views

urlpatterns = [
    path('',views.register,name="register"),
    path('index',views.index,name="index"),
    path('login',views.login_view,name="login"),
    path('product_review',views.product_review,name="product_review"),
    path('product_view',views.product_view,name="product_view"),
    path('insert', views.insertData,name="insertData"),
    path('delete/<id>',views.deleteData,name="deleteData"),
    path('update/<id>',views.updateData,name="updateData"),
    
    
]