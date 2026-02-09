from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomUserSerializer, JournalEntrySerializer, DailyGoalsSerializer, HydrationTrackerSerializer
from .models import CustomUser, JournalEntry, DailyGoals, HydrationTracker

# Create your views here.
class CustomUserView(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class JournalEntryView(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    queryset = JournalEntry.objects.all()

class DailyGoalsView(viewsets.ModelViewSet):
    serializer_class = DailyGoalsSerializer
    queryset = DailyGoals.objects.all()

class HydrationTrackerView(viewsets.ModelViewSet):
    serializer_class = HydrationTrackerSerializer
    queryset = HydrationTracker.objects.all()