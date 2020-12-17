from django.urls import path
from tempapp import views

app_name='tempapp'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('others/',views.others,name='others'),
]
