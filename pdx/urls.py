from django.urls import path
from .views import (
    homepage, submit_model, model_submitted, pdx_list, pdx_detail
)


urlpatterns = [
    path('', homepage, name='home'),
    path('submit/', submit_model, name='submit'),
    path('submit/model_submitted.html', model_submitted, name='model_submitted'),
    path('data/', pdx_list, name='data'),
    path('data/<pk>/', pdx_detail, name='model_detail'),
]
