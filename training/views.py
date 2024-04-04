from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Activity, UserActivity,UserActivityLog
from .serializers import UserActivitySerializer,UserActivityLogSerializer, ActivitySerializer
from rest_framework import serializers, viewsets

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
class UserActivityLogViewSet(viewsets.ModelViewSet):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer
