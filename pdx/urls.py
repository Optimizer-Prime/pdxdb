from django.urls import path
from .views import (
    homepage_view,
    submit_model_view,
    model_submitted_view,
    pdx_list_view,
    pdx_detail_view,
)


urlpatterns = [
    path('', homepage_view, name='home'),
    path('submit/', submit_model_view, name='submit'),
    path('submit/model_submitted.html', model_submitted_view, name='model_submitted'),
    path('data/', pdx_list_view, name='data'),
    path('data/<model_id>/', pdx_detail_view, name='model_detail'),
]
