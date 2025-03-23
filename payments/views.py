from django.shortcuts import render

def welcome_page(request):
    return render(request, 'welcome.html')

def user_info_page(request):
    return render(request, 'user_info.html')

def payment_method_page(request):
    return render(request, 'payment_method.html')

def payment_details_page(request):
    return render(request, 'payment_details.html')

def payment_success_page(request):
    return render(request, 'payment_success.html')
