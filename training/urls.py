from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserActivityViewSet, ActivityViewSet

router = DefaultRouter()
router.register(r'/activities', ActivityViewSet)
router.register(r'/useractivities', UserActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]