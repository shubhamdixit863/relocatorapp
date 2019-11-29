from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id=request.POST["listing_id"]
        listing=request.POST["listing"]
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]
        user_id=request.POST["user_id"]
        realtor_email=request.POST["realtor_email"]
        #Check if user has already made enquiry
        if request.user.is_authenticated:
            user_id=request.user.id 
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You have Already Contacted For This Property")
                return redirect('/listings/'+listing_id)
                
        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,user_id=user_id,message=message)
        contact.save()
        send_mail(
         'Property Listing Enquiry',
          'There Has Been An Enquiry For '+listing+'Sign In to Admin Panel To See More',
           'searchingmyself660@gmail.com',
          ['searchingmyself660@gmail.com','searchingmyself660@gmail.com'],
          fail_silently=True,
          )
        messages.success(request,"We will Get Back To You Soon")
        return redirect('/listings/'+listing_id)
