from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Activity, UserActivity
from .serializers import UserActivitySerializer, ActivitySerializer
from rest_framework import serializers, viewsets

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer