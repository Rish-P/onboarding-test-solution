from django.shortcuts import render
from django.db.models import Q
from .models import Activity, UserActivity,UserActivityLog, do_training
from django.contrib.auth.models import User
from .serializers import UserActivitySerializer,UserActivityLogSerializer, ActivitySerializer, UserSerializer, UserRegistrationSerializer
from rest_framework.exceptions import MethodNotAllowed
from rest_framework import serializers, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from collections import defaultdict

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

class TaskInfo(APIView):

    def get(self, request):
        activity_id = request.GET.get('activity')
        user_id = request.GET.get('user')
        
        # Build the filter conditions using Q objects
        filter_conditions = Q()
        if activity_id:
            filter_conditions &= Q(activity_id=activity_id)
        if user_id:
            filter_conditions &= Q(user_id=user_id)

        # Apply the filter conditions to the query
        user_activities = UserActivity.objects.filter(filter_conditions)

        # Prefetch related UserActivityLogs for all UserActivities
        user_activities = user_activities.prefetch_related('useractivitylog_set')

        # Create a defaultdict to collect scores grouped by user_id and activity_id
        scores_dict = defaultdict(list)
        for user_activity in user_activities:
            user_id = user_activity.user_id
            activity_id = user_activity.activity_id
            user_scores = user_activity.useractivitylog_set.first().score
            scores_dict[(user_id, activity_id)].append(user_scores)
        
        # Convert the scores dictionary into the desired response format
        response_data = [{'user_id': user_id, 'activity_id': activity_id, 'scores': scores} 
                        for (user_id, activity_id), scores in scores_dict.items()]
        
        return Response(response_data)
