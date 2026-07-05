from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'market'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('subscribe/', views.subscription_checkout, name='subscription_checkout'),
    path('subscribe/success/', views.payment_success, name='payment_success'),
    path('api/create-order/', views.create_paypal_order, name='create_paypal_order'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='market/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]