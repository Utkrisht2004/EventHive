from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event-list'),  # ✅ This must match exactly
    path('register/<int:event_id>/', views.register_for_event, name='register_for_event'),
]
