from django.shortcuts import render
from .models import Activity, UserActivity,UserActivityLog, do_training
from django.contrib.auth.models import User
from .serializers import UserActivitySerializer,UserActivityLogSerializer, ActivitySerializer, UserSerializer, UserRegistrationSerializer
from rest_framework.exceptions import MethodNotAllowed
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

    def perform_create(self, serializer):
        instance = serializer.save()
        # Create and save UserActivityLog instance
        UserActivityLog.objects.create(user_activity=instance, score = do_training())

class UserActivityLogViewSet(viewsets.ModelViewSet):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed("POST")

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

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)