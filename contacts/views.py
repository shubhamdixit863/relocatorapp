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
            title= "Not Mentioned" or request.POST["title"]
            fname= "Not Mentioned" or request.POST["fname"]
            lname="Not Mentioned" or request.POST["lname"]
            service_type= "NOT MENTIONED" or request.POST["service_type"]
            name="{} {} {}".format(title,fname,lname)
            email="Not Mentioned" or request.POST["email"]
            phone= "Not Mentioned" or request.POST["phone"]
            movedate= "Not Mentioned" or request.POST["move_date"]
            propsize= "Not Mentioned" or request.POST["prop_size"]
            appoint_date= "Not Mentioned" or request.POST["appointment_date"]
            moving_city="Not Mentioned" or request.POST["moving_city"]
            destination_city="Not Mentioned" or request.POST["destination_city"]
            phone="Not Mentioned" or request.POST["phone"]
            msg="Not Mentioned" or request.POST["msg"]
            message="Hello, I am looking to move  from {}  to {} on {} I need an appointment for {}.My luggage is {} .My Service Type is {} .Comments {}".format(moving_city,destination_city,movedate,appoint_date,propsize,service_type,msg)
            user_id=request.POST["user_id"]
       # realtor_email=request.POST["realtor_email"]
        #Check if user has already made enquiry
            if request.user.is_authenticated:
                user_id=request.user.id 
           
                
            contact=Contact(name=name,email=email,phone=phone,user_id=user_id,message=message)
            contact.save()
            """
            send_mail(
           'Property Listing Enquiry',
           'There Has Been An Enquiry For Sign In to Admin Panel To See More',
           'searchingmyself660@gmail.com',
            ['searchingmyself660@gmail.com','searchingmyself660@gmail.com'],
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
               response = sg.send(messageadmin)
               print(response.status_code)
               print(response.body)
               print(response.headers)
            except Exception as e:
               print("This e"+e)
            messages.success(request,"We will Get Back To You Soon")
            return redirect('requestquote')
    except Exception as e: 
        print(e)
        messages.error(request,"Please ensure that you input correct data")
        return redirect('requestquote')




# Create your views here.
def contactenquiry(request):
    try:
        app_url = request.path
        if request.method == 'POST':
            title= "Not Mentioned" or request.POST["title"]
            fname= "Not Mentioned" or request.POST["fname"]
            lname="Not Mentioned" or request.POST["lname"]
            service_type= "NOT MENTIONED" or request.POST["service_type"]
            name="{} {} {}".format(title,fname,lname)
            email="Not Mentioned" or request.POST["email"]
            phone= "Not Mentioned" or request.POST["phone"]
            movedate= "Not Mentioned" or request.POST["move_date"]
            propsize= "Not Mentioned" or request.POST["prop_size"]
            appoint_date= "Not Mentioned" or request.POST["appointment_date"]
            moving_city="Not Mentioned" or request.POST["moving_city"]
            destination_city="Not Mentioned" or request.POST["destination_city"]
            phone="Not Mentioned" or request.POST["phone"]
            msg="Not Mentioned" or request.POST["msg"]
            message="Hello, I am looking to move  from {}  to {} on {} I need an appointment for {}.My luggage is {} .My Service Type is {} .Comments {}".format(moving_city,destination_city,movedate,appoint_date,propsize,service_type,msg)
            user_id=request.POST["user_id"]
       # realtor_email=request.POST["realtor_email"]
        #Check if user has already made enquiry
            if request.user.is_authenticated:
                user_id=request.user.id 
           
                
            contact=Contact(name=name,email=email,phone=phone,user_id=user_id,message=message)
            contact.save()
            """
            send_mail(
           'Property Listing Enquiry',
           'There Has Been An Enquiry For Sign In to Admin Panel To See More',
           'searchingmyself660@gmail.com',
            ['searchingmyself660@gmail.com','searchingmyself660@gmail.com'],
            fail_silently=True,
             )
             """
            message = Mail(
            from_email='info@relocatoremovals.in',
            to_emails='shubhamdixit863@gmail.com',
            subject='Hey,Thanks For Saying Us Hi !!!',
            html_content=htmlcontent)
            message = Mail(
            from_email='info@relocatoremovals.in',
            to_emails='info@relocatoremovals.in',
            subject='A new Enquiry Has Arrived',
            html_content="Hi Admin ,You have a Enquiry From Client ,Login To Admin Panel To See More")
            try:
               sg = SendGridAPIClient('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')
               response = sg.send(message)
               response = sg.send(message)
               print(response.status_code)
               print(response.body)
               print(response.headers)
            except Exception as e:
               print("This e"+e)
            messages.success(request,"We will Get Back To You Soon")
            return redirect('requestquote')
    except Exception as e: 
        print(e)
        messages.error(request,"Please ensure that you input correct data")
        return redirect('requestquote')