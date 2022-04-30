
from .import views
from django.urls import path
urlpatterns = [
    path('',views.Home1),
    path('mens/',views.Mens),
    path('womens/',views.Womens),
    path('kids/',views.Kids),
    path('accessories/',views.Accessories),
    path('contact/',views.ContactUs),
    path('cartpage/',views.Cartpage),
    path('checkout/',views.Checkout),
    path('submitcheckout/',views.submitcheckout),
    # Details modul starts
    path('mens/detail/<int:id>',views.Detail_mens,name="product_detail"),
    path('womens/detail/<int:id>',views.Detail_womens),
    path('kids/detail/<int:id>',views.Detail_kids),
    path('accessories/detail/<int:id>',views.Detail_accessories),
    # Details modul ends 

    

    path('signin/',views.Signin),
    path('login/',views.Login),
    path('signindo/',views.Signindo),
    path('logindo/',views.Logindo),

    path('Qrdetails/',views.Qrdetails),
    path('Qrdetailsubmitted/',views.Qrdetailsubmitted),


    path('contactus/',views.contactusboi),
    path('contactsubmitted/',views.Contactsubmit),


    # logout 
    path('logout/',views.logoutkaro),

    # search bar
    path('search',views.search,name='search'),
    path('searchwomens',views.searchwomens,name='search'),
    path('searchkids',views.searchkids,name='search'),
    path('searchaccessories',views.searchaccessories,name='search'),
    
    #review 
    path('review',views.Review_Rate,name='review'),
    path('deliverydone',views.deliverydone,name='deliverydone'),
  
]
