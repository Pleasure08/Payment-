// Function to initialize Paystack
   function initializePaystack() {
       const email = document.getElementById('email').value;
       const amount = document.getElementById('amount').value * 100; // Convert to kobo

       const handler = PaystackPop.setup({
           key: 'pk_live_72f3eb0020f924a29d293ddbe5c058caab352b66', // Replace with your Paystack public key
           email: email,
           amount: amount,
           currency: 'NGN',
           callback: function(response) {
               alert('Payment successful! Reference: ' + response.reference);
           },
           onClose: function() {
               alert('Payment window closed.');
           }
       });

       handler.openIframe();
   }

   // Function to check if Paystack is loaded
   function checkPaystackLoaded() {
       if (typeof PaystackPop !== 'undefined') {
           // Paystack is loaded, initialize the payment form
           document.getElementById('paymentForm').addEventListener('submit', function(e) {
               e.preventDefault();
               document.getElementById('loading').style.display = 'block'; // Show loading indicator
               initializePaystack();
           });
       } else {
           // Paystack is not loaded yet, retry after 500ms
           setTimeout(checkPaystackLoaded, 500);
       }
   }

   // Start checking if Paystack is loaded
   checkPaystackLoaded();
