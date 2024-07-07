
from django.urls import path
from . import views
urlpatterns = [
   path(
       '',views.home,name='home',
       
   ),
   path(
       'aboutus/',views.aboutus,name='aboutus'
   ),
    path(
       'service/',views.service,name='service'
   ),
   path(
       'department/',views.department,name='department'
   ),
    path(
       'contact/',views.contact,name='contact'
   )
   ,
    path(
       'appointment/',views.appointment,name='appointment'
   ),
   path(
        'success/', views.success, name="success"
    )
]
