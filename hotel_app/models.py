from importlib.metadata import requires

from django.db import models

# Create your models here.
from django.db import models

class Room(models.Model):
    BED_TYPE_CHOICES = [
        ('', 'Select'),
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Queen', 'Queen'),
        ('King', 'King'),
    ]

    SMOKING_CHOICES = [
        ('', 'Select'),
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    occupant_name = models.CharField(max_length=20, blank=True, null=True)
    room_number = models.IntegerField(unique=True, blank=False, null=False)
    bed_type = models.CharField(max_length=20, choices=BED_TYPE_CHOICES, blank=False, null=False, default='')
    smoking = models.CharField(max_length=15, choices=SMOKING_CHOICES, default='')
    rate = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

