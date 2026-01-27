from django.contrib import admin
from .models import CustomUser, JournalEntry, DailyGoals, HydrationTracker

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(JournalEntry)
admin.site.register(DailyGoals)
admin.site.register(HydrationTracker)

