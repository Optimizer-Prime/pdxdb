from django.urls import path
from .views import homePageView, submitModelsView


urlpatterns = [
    path('', homePageView, name='home'),
    path('submit/', submitModelsView, name='submit'),
]
