from django.shortcuts import render
from django.http import HttpResponse
 # Create your views here.
def index(request):
    return render(request,'pages/index.html')

def about(request):
   return render(request,'pages/about.html')

def internationalrelocations(request):
   return render(request,'pages/internationalrelocations.html')

def indiarelocations(request):
   return render(request,'pages/indiarelocations.html')

def resources(request):
   return render(request,'pages/resources.html')

def bookasurvey(request):
   return render(request,'pages/bookasurvey.html')

def commercialmoves(request):
   return render(request,'pages/commercialmoves.html')

def hospitalitylogistics(request):
   return render(request,'pages/hospitalitylogistics.html')

def officemoves(request):
   return render(request,'pages/officemoves.html')

def valetservice(request):
   return render(request,'pages/valetservice.html')

def treesrelocation(request):
   return render(request,'pages/treesrelocation.html')

def fineartmoving(request):
   return render(request,'pages/fineartmoving.html')

def carshifting(request):
   return render(request,'pages/carshifting.html')

def orientationservices(request):
   return render(request,'pages/orientationservices.html')

def worldclassstorage(request):
   return render(request,'pages/worldclassstorage.html')

def withincity(request):
   return render(request,'pages/withincity.html')

def petrelocation(request):
   return render(request,'pages/petrelocation.html')

#Tracking

def tracking(request):
   return render(request,'pages/tracking.html')

def volumecalculator(request):
   return render(request,'pages/volumecalculator.html')

def claims(request):
   return render(request,'pages/claims.html')

def insurance(request):
   return render(request,'pages/insurance.html')

def usefulinformation(request):
   return render(request,'pages/usefulinformation.html')

def industryinformation(request):
   return render(request,'pages/industryinformation.html')

def custominformation(request):
   return render(request,'pages/custominformation.html')

def generalinformation(request):
   return render(request,'pages/generalinformation.html')

########################
def usefultools(request):
   return render(request,'pages/usefultools.html')

def blog(request):
   return render(request,'pages/blog.html')


def onlinepayment(request):
   return render(request,'pages/onlinepayment.html')

def customervideos(request):
   return render(request,'pages/customervideos.html')

def gallery(request):
   return render(request,'pages/gallery.html')

def contactus(request):
   return render(request,'pages/contactus.html')

def requestquote(request):
   return render(request,'pages/requestquote.html')

def services(request):
   return render(request,'pages/services.html')

def enquiry(request):
   return render(request,'pages/enquiry.html')

def privacypolicy(request):
   return render(request,'pages/privacypolicy.html')

def termsconditions(request):
   return render(request,'pages/termsconditions.html')

def faq(request):
   return render(request,'pages/faq.html')

def testimonials(request):
   return render(request,'pages/testimonials.html')

def disclaimer(request):
   return render(request,'pages/disclaimer.html')

def state(request,statename):
   app_url = request.path
   print(statename)
   return render(request,'pages/{}.html'.format(statename))


    
    
   
   
  
    
  
    
   
   
    
  
   
    
