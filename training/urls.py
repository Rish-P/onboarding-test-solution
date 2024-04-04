from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserActivityViewSet,UserActivityLogViewSet, ActivityViewSet, UserInfoView, UserViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'useractivities', UserActivityViewSet)
router.register(r'useractivitieslogs', UserActivityLogViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-info/', UserInfoView.as_view(), name='user-info'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]