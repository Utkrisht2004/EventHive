from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Registration
from .forms import RegistrationForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Check if user already registered
    existing_registration = Registration.objects.filter(event=event, attendee=request.user).first()
    if existing_registration:
        messages.error(request, "You have already registered for this event.")
        return redirect('event-list')  # Ensure this is correct

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.attendee = request.user
            registration.event = event
            registration.save()
            messages.success(request, "You have successfully registered!")
            return redirect('event-list')  # Ensure this matches `urls.py`
    else:
        form = RegistrationForm()

    return render(request, 'events/register_event.html', {'form': form, 'event': event})
