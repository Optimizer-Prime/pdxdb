from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PdxViewSet


router = SimpleRouter()
router.register('', PdxViewSet, basename='posts')

urlpatterns = router.urls
