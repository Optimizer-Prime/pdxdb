from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PdxViewSet


router = SimpleRouter()
router.register('', PdxViewSet, basename='pdxs')

urlpatterns = [
    path('', include(router.urls)),
]
