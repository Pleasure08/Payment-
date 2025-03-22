from django.shortcuts import render, redirect
   from .forms import PaymentForm  # Import the form

   def payment_view(request):
       if request.method == 'POST':
           form = PaymentForm(request.POST)  # Bind the form to POST data
           if form.is_valid():
               # Process the form data
               name = form.cleaned_data['name']
               email = form.cleaned_data['email']
               amount = form.cleaned_data['amount']
               # Redirect to Paystack payment page (replace with your logic)
               return redirect('https://paystack.com/payment-page-url')
       else:
           form = PaymentForm()  # Create an empty form for GET requests
       return render(request, 'payment_form.html', {'form': form})
