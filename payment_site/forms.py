from django import forms

   class PaymentForm(forms.Form):
       name = forms.CharField(
           max_length=100,
           label='Full Name',
           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'})
       )
       email = forms.EmailField(
           label='Email Address',
           widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
       )
       amount = forms.DecimalField(
           label='Amount (NGN)',
           widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the amount'})
       )
