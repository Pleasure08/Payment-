from django.urls import path
from . import views  # Make sure there's no indentation here

urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    path('user-info/', views.user_info_page, name='user_info'),
    path('payment-method/', views.payment_method_page, name='payment_method'),
    path('payment-details/', views.payment_details_page, name='payment_details'),
    path('payment-success/', views.payment_success_page, name='payment_success'),
]
