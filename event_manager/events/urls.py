from django.urls import path
from .views import event_list, register_for_event

urlpatterns = [
    path("", event_list, name="event-list"),  
    path("register/<int:event_id>/", register_for_event, name="register_for_event"),
]
