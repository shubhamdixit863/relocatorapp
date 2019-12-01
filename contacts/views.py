from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.contrib.staticfiles.templatetags.staticfiles import static
logo= static('images/logo.png')
banner= static('images/happy-client.jpg')
htmlcontent='<p>&nbsp;</p> <p>&nbsp;</p> <table border="1" width="95%%" cellspacing="0" cellpadding="0" align="center"> <tbody> <tr> <td align="center"> <table style="border-collapse: separate; border-spacing: 2px 5px; box-shadow: 1px 0 1px 1px #B8B8B8;" border="1" width="600" cellspacing="0" cellpadding="0" align="center" bgcolor="#FFFFFF"> <tbody> <tr> <td style="padding: 5px 5px 5px 5px;" align="center"><a href="http://url-goes-here" target="_blank" rel="noopener"> <img style="width: 186px; border: 0;" src="{}" alt="Logo" /> </a></td> </tr> <tr> <td align="center"><!-- Initial relevant banner image goes here under src--> <img style="display: block; border: 0;" src="{}" alt="Image Banner" width="600" height="100%%" /></td> </tr> <tr> <td style="padding: 40px 30px 40px 30px;" bgcolor="#ffffff"> <table border="1" width="100%%" cellspacing="0" cellpadding="0"> <tbody> <tr> <td style="padding: 10px 0 10px 0; font-family: Avenir, sans-serif; font-size: 16px;">Hi ,there ,Thanks For Showing Interest in Relocato. Our Team will Connect With You Soon . Happy Relocating !!</td> </tr> </tbody> </table> </td> </tr> <tr> <td bgcolor="#E8E8E8"> <table style="padding: 20px 10px 10px 10px;" border="1" width="100%%" cellspacing="0" cellpadding="0"> <tbody> <tr> <td style="padding: 0 0 15px 0;" valign="top" width="260"> <table border="1" width="100%%" cellspacing="0" cellpadding="0"> <tbody> <tr> </tr> <tr> <td style="font-family: Avenir, sans-serif; color: #707070; font-size: 13px; padding: 10px 0 0 0;" align="center">7982940347</td> </tr> </tbody> </table> </td> <td style="font-size: 0; line-height: 0;" width="20">&nbsp;</td> <td valign="top" width="260"> <table border="1" width="100%%" cellspacing="0" cellpadding="0"> <tbody> <tr> </tr> <tr> <td style="font-family: Avenir, sans-serif; color: #707070; font-size: 13px; padding: 10px 0 0 0;" align="center">Support@Relocatopackers.com</td> </tr> </tbody> </table> </td> <td style="font-size: 0; line-height: 0;" width="20">&nbsp;</td> <td valign="top" width="260"> </td> </tr> </tbody> </table> </td> </tr> <tr> <td style="padding: 15px 15px 15px 15px;" bgcolor="#66989c"> <table border="1" width="100%%" cellspacing="0" cellpadding="0"> <tbody> <tr> <td align="center"> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table> <p>&copy; 2019 Relocato, Inc.</p>'.format(logo,banner)

# Create your views here.
def contact(request):
    try:
        app_url = request.path
        if request.method == 'POST':
            name=request.POST["name"]
            email=request.POST["email"]
            phone=request.POST["phone"]
            movedate=request.POST["move_date"]
            propsize=request.POST["currentfloor"]
            moving_city=request.POST["from"]
            destination_city=request.POST["to"]
            l1=request.POST["liftsource"]
            l2=request.POST["liftsourcedestination"]
            l1=request.POST["currentfloordestination"]
            msg=request.POST["msg"]
            message="Hello, I am looking to move  from {}  to {} on {} I need an appointment for {}.My luggage is {} .My Service Type is {} .Comments {}".format(moving_city,destination_city,movedate,l1,propsize,l2,msg)
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
            'info@relocatoremovals.in',
            ['info@relocatoremovals.in'],
            fail_silently=True,
             )
            send_mail(
           'Property Listing Enquiry',
           'Thanks For Showing Interest in Our Services .Our Team Will Get In Touch With You Soon',
           'info@relocatoremovals.in',
            [email],
            fail_silently=True,
             )
            """
            print("email submiteed"+email)
            message = Mail(
            from_email='info@relocatoremovals.in',
            to_emails=email,
            subject='Hey,Thanks For Saying Us Hi !!!',
            html_content=htmlcontent)
            messageadmin = Mail(
            from_email='info@relocatoremovals.in',
            to_emails='info@relocatoremovals.in',
            subject='A new Enquiry Has Arrived',
            html_content="Hi Admin ,You have a Enquiry From Client ,Login To Admin Panel To See More")
            try:
               sg = SendGridAPIClient('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')
               response = sg.send(message)
               response = sg.send(messageadmin)
               print(response.status_code)
               print(response.body)
               print(response.headers)
            except Exception as e:
               print("This e"+e)
            """
            messages.success(request,"We will Get Back To You Soon")
            return redirect('enquiry')
    except Exception as e: 
        print(e)
        messages.error(request,"Please ensure that you input correct data")
        return redirect('enquiry')




# Create your views here.
def contactenquiry(request):
    try:
        app_url = request.path
        if request.method == 'POST':
            name=request.POST["name"]
          
            email=request.POST["email"]
            phone=request.POST["phone"]
           
            msg=request.POST["msg"]
            
            user_id=request.POST["user_id"]
            print(user_id)
       # realtor_email=request.POST["realtor_email"]
        #Check if user has already made enquiry
            if request.user.is_authenticated:
                user_id=request.user.id 
           
                
            contact=Contact(name=name,email=email,phone=phone,user_id=user_id,message=msg)
            contact.save()
            
            send_mail(
           'Property Listing Enquiry',
           'There Has Been An Enquiry For Sign In to Admin Panel To See More',
           'info@relocatoremovals.in',
            ['info@relocatoremovals.in'],
            fail_silently=True,
             )
            send_mail(
           'Property Listing Enquiry',
           'Thanks For Showing Interest in Our Services .Our Team Will Get In Touch With You Soon',
           'info@relocatoremovals.in',
            [email],
            fail_silently=True,
             )
            """
            message = Mail(
            from_email='info@relocatoremovals.in',
            to_emails=email,
            subject='Hey,Thanks For Saying Us Hi !!!',
            html_content=htmlcontent)
            messageadmin = Mail(
            from_email='info@relocatoremovals.in',
            to_emails='info@relocatoremovals.in',
            subject='A new Enquiry Has Arrived',
            html_content="Hi Admin ,You have a Enquiry From Client ,Login To Admin Panel To See More")
            try:
               sg = SendGridAPIClient('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')
               response = sg.send(message)
              # response = sg.send(messageadmin)
               print(response.status_code)
               print(response.body)
               print(response.headers)
            except Exception as e:
               print("This e"+e)
            """
            messages.success(request,"We will Get Back To You Soon")
            return redirect('contactus')
    except Exception as e: 
        print(e)
        messages.error(request,"Please ensure that you input correct data")
        return redirect('contactus')