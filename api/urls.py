from django.urls import path
from .views import PdxAPIView


urlpatterns = [
    path('', PdxAPIView.as_view()),
]
