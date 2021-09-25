import uuid

from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django.conf import settings

# https://docs.djangoproject.com/en/3.2/ref/models/fields/

class Weddingevent(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person1 = models.CharField(max_length=300)
    person2 = models.CharField(max_length=300)
    greeting = models.TextField(blank=True)
    blurb = models.TextField(blank=True)
    body = models.TextField(blank=True)
    location = models.TextField(blank=True)
    meetingURL = models.CharField(max_length=1000)
    time_and_date = models.DateTimeField()
    notepad = models.TextField(blank=True)
    template_name = models.CharField(max_length=800,default="default")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        toret = f"Wedding of { self.person1 } and { self.person2 } at { self.time_and_date }"
        return toret

    class Meta:
        verbose_name_plural = "Weddings"
        verbose_name = "Wedding"


class Party(models.Model):
    """
    A party consists of one or more guests.
    """
    wedding = models.ForeignKey('Weddingevent', on_delete=models.CASCADE)
    invitation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invite_code_short = models.CharField(max_length=10, null=True, unique=True)
    invite_code_long = models.UUIDField(default=uuid.uuid4)
    name = models.TextField()
    category = models.CharField(max_length=30, null=True, blank=True)
    save_the_date_sent = models.DateTimeField(null=True, blank=True, default=None)
    save_the_date_opened = models.DateTimeField(null=True, blank=True, default=None)
    invitation_sent = models.DateTimeField(null=True, blank=True, default=None)
    invitation_opened = models.DateTimeField(null=True, blank=True, default=None)
    comments = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Party: {}'.format(self.name)


    @property
    def ordered_guests(self):
        return self.guest_set.order_by('is_child', 'pk')

    @property
    def any_guests_attending(self):
        return any(self.guest_set.values_list('is_attending', flat=True))

    @property
    def guest_emails(self):
        return list(filter(None, self.guest_set.values_list('email', flat=True)))

    class Meta:
        verbose_name_plural = "Parties"
        verbose_name = "Party"



class Guest(models.Model):
    """
    A single guest
    """
    MEAL_CHOICES = [
        ("VEGETARIAN", 'Vegetarian'),
        ("VEGAN", 'Vegan'),
        ("BEEF", 'beef'),
        ("FISH", 'fish'),
        ("NO PREF", 'No Preference'),
    ]
    party = models.ForeignKey('Party', on_delete=models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    is_attending = models.BooleanField(null=True)
    meal_prefs = models.CharField(
        max_length=100,
        choices=MEAL_CHOICES,
        default="NO PREF",
    )
    kosher_meal = models.BooleanField(default=True)
    is_child = models.BooleanField(default=False)

    @property
    def name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    @property
    def unique_id(self):
        # convert to string so it can be used in the "add" templatetag
        return str(self.pk)

    def __str__(self):
        return 'Guest: {} {}'.format(self.first_name, self.last_name)


