from django.urls import path
from .views import (
    homePageView, submitModelsView, modelSubmittedView, dataView, dataDetailView
)


urlpatterns = [
    path('', homePageView, name='home'),
    path('submit/', submitModelsView, name='submit'),
    path('submit/model_submitted.html', modelSubmittedView, name='model_submitted'),
    path('data/', dataView, name='data'),
    path('data/<pk>/', dataDetailView, name='data_detail'),
]
