# Create your views here.
from django.shortcuts import render, redirect
from .models import Event, Registration
from django.contrib.auth.decorators import login_required

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def register_for_event(request, event_id):
    event = Event.objects.get(id=event_id)
    Registration.objects.create(event=event, attendee=request.user)
    return redirect('event_list')
