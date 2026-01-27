from rest_framework import serializers
from .models import CustomUser, JournalEntry, DailyGoals, HydrationTracker

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'google_id', 'username', 'email', 'password', 'first_name', 'is_staff', 'is_superuser')

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ('id', 'user', 'title', 'journal_content', 'date_created')

class DailyGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGoals
        fields = ('id', 'user', 'title', 'consecutive_submissions', 'submissions_total', 'date_submitted')

class HydrationTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydrationTracker
        fields = ('id', 'user', 'water_intake', 'max_water', 'date_of_intake')