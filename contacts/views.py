from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    try:

        if request.method == 'POST':
            title=request.POST["title"]
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            service_type= "NOT MENTIONED" or request.POST["service_type"]
            name="{} {} {}".format(title,fname,lname)
            email=request.POST["email"]
            phone=request.POST["phone"]
            movedate=request.POST["move_date"]
            propsize= "Not Mentioned" or request.POST["prop_size"]
            appoint_date= "Not Mentioned" or request.POST["appointment_date"]
            moving_city=request.POST["moving_city"]
            destination_city=request.POST["destination_city"]
            phone=request.POST["phone"]
            msg="Not Mentioned" or request.POST["msg"]
            message="Hello, I am looking to move  from {}  to {} on {} I need an appointment for {}.My luggage is {} .My Service Type is {} .Comments {}".format(moving_city,destination_city,movedate,appoint_date,propsize,service_type,msg)
            user_id=request.POST["user_id"]
       # realtor_email=request.POST["realtor_email"]
        #Check if user has already made enquiry
            if request.user.is_authenticated:
                user_id=request.user.id 
           
                
            contact=Contact(name=name,email=email,phone=phone,user_id=user_id,message=message)
            contact.save()
            send_mail(
           'Property Listing Enquiry',
           'There Has Been An Enquiry For Sign In to Admin Panel To See More',
           'searchingmyself660@gmail.com',
            ['searchingmyself660@gmail.com','searchingmyself660@gmail.com'],
            fail_silently=True,
             )
            messages.success(request,"We will Get Back To You Soon")
            return redirect('requestquote')
    except Exception as e: 
        print(e)
        messages.error(request,"Please ensure that you input correct data")
        return redirect('requestquote')