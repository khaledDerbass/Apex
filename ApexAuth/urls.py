from django.urls import path
from ApexAuth import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.handlelogin, name='handlelogin'),
    path('logout/',views.handlelogin, name='handlelogout'),
    path('resetpass/',views.resetpassword, name='resetpassword'),

]
