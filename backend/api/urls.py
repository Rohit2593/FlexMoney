from django.urls import path 
from .views import DataValidation

urlpatterns = [
    path('make-payment/', DataValidation.as_view(), name='make_payment')
]