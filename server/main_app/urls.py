from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'journal-entry/', views.JournalEntryView, 'journal-entry')
router.register(r'users', views.CustomUserView, 'user')
router.register(r'daily-goals', views.DailyGoalsView, 'daily-goals')
router.register(r'hydration-tracker', views.HydrationTrackerView, 'hydration-tracker')

urlpatterns = [
    path('api/', include(router.urls)),
]