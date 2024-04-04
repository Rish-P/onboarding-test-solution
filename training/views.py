from django.shortcuts import render
from .models import Activity, UserActivity,UserActivityLog
from django.contrib.auth.models import User
from .serializers import UserActivitySerializer,UserActivityLogSerializer, ActivitySerializer, UserSerializer
from rest_framework import serializers, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer

class UserActivityLogViewSet(viewsets.ModelViewSet):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer

class UserInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for all actions
