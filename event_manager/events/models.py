from django.db import models
from django.contrib.auth.models import User
import re
import random
import string

def generate_unique_reg_number():
    """Generate a unique registration number (AB1234)"""
    while True:
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))  # 2 random letters
        numbers = ''.join(random.choices(string.digits, k=4))  # 4 random digits
        reg_number = letters + numbers
        if not Registration.objects.filter(registration_number=reg_number).exists():
            return reg_number

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Unknown")  
    registration_number = models.CharField(max_length=6, unique=True, blank=True)  # No default here
    email = models.EmailField(default="default@example.com")  

    def __str__(self):
        return f"{self.name} registered for {self.event.title}"

    def save(self, *args, **kwargs):
        """ Ensure registration number follows the correct format and is unique """
        if not self.registration_number:  # Generate only if not provided
            self.registration_number = generate_unique_reg_number()

        if not re.match(r'^[A-Z]{2}\d{4}$', self.registration_number):
            raise ValueError("Registration number must be in format AB1234")

        super().save(*args, **kwargs)
