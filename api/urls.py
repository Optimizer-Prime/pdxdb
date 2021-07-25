from django.urls import path
from .views import PdxListView, PdxDetailView


urlpatterns = [
    path('<str:pk>/', PdxDetailView.as_view()),
    path('', PdxListView.as_view()),
]
