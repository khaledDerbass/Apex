from django.urls import path
from ApexComme import views
urlpatterns = [
    path('',views.index, name='index')
]
