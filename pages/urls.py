from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('internationalrelocations',views.internationalrelocations,name='internationalrelocations'),
    path('indiarelocations',views.indiarelocations,name='indiarelocations'),
    path('withincity',views.withincity,name='withincity'),
    path('carshifting',views.carshifting,name='carshifting'),
    path('worldclassstorage',views.worldclassstorage,name='worldclassstorage'),
    path('fineartmoving',views.fineartmoving,name='fineartmoving'),
    path('orientationservices',views.orientationservices,name='orientationservices'),
    path('petrelocation',views.petrelocation,name='petrelocation'),
    path('treesrelocation',views.treesrelocation,name='treesrelocation'),
    path('valetservice',views.valetservice,name='valetservice'),
    path('officemoves',views.officemoves,name='officemoves'),
    path('hospitalitylogistics',views.hospitalitylogistics,name='hospitalitylogistics'),
    path('commercialmoves',views.commercialmoves,name='commercialmoves'),
    path('bookasurvey',views.bookasurvey,name='bookasurvey'),
    path('resources',views.resources,name='resources'),
    # Tracking
    path('tracking',views.tracking,name='tracking'),
    path('volumecalculator',views.volumecalculator,name='volumecalculator'),
    path('claims',views.claims,name='claims'),
    path('insurance',views.insurance,name='insurance'),
    path('usefulinformation',views.usefulinformation,name='usefulinformation'),
    path('industryinformation',views.industryinformation,name='industryinformation'),
    path('custominformation',views.custominformation,name='custominformation'),
    path('generalinformation',views.generalinformation,name='generalinformation'),
    # Resources
    path('usefultools',views.usefultools,name='usefultools'),
    path('blog',views.blog,name='blog'),
    path('onlinepayment',views.onlinepayment,name='onlinepayment'),
    path('customervideos',views.customervideos,name='customervideos'),
    path('gallery',views.custominformation,name='gallery'),
    path('contactus',views.contactus,name='contactus'),
    path('requestquote',views.requestquote,name='requestquote'),
    path('services',views.services,name='services'),#
    path('enquiry',views.enquiry,name='enquiry'),#
    path('privacypolicy',views.privacypolicy,name='privacypolicy'),#
    path('faq',views.faq,name='faq'),#
    path('disclaimer',views.disclaimer,name='disclaimer'),#
    path('termsconditions',views.termsconditions,name='termsconditions'),#
    path('testimonials',views.testimonials,name='testimonials'),#
    path('packers/<slug:statename>/', views.state,name="packers")
    
    ]
    

      
                
      
                  
      
                  
      
                  
      
               
      
                   
      
                  
                  
      
                
      
 

    
