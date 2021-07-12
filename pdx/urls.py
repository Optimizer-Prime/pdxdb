from django.urls import path
from .views import homePageView, submitModelsView, modelSubmittedView


urlpatterns = [
    path('', homePageView, name='home'),
    path('submit/', submitModelsView, name='submit'),
    path('submit/model_submitted.html', modelSubmittedView, name='model_submitted'),
]
