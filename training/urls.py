from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserActivityViewSet,UserActivityLogViewSet, ActivityViewSet

router = DefaultRouter()
router.register(r'/activities', ActivityViewSet)
router.register(r'/useractivities', UserActivityViewSet)
router.register(r'/useractivitieslog', UserActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]