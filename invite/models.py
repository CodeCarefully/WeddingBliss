import uuid

from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django.conf import settings
import re
from django.template.defaultfilters import slugify

# https://docs.djangoproject.com/en/3.2/ref/models/fields/

class Weddingevent(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(blank=True)
    person1 = models.CharField(max_length=300)
    person2 = models.CharField(max_length=300)
    greeting = models.TextField(blank=True)
    blurb = models.TextField(blank=True)
    body = models.TextField(blank=True)
    location = models.TextField(blank=True)
    meetingURL = models.CharField(max_length=1000,blank=True)
    autotriggerdomain = models.CharField(max_length=1000, blank=True)
    time_and_date = models.DateTimeField()
    notepad = models.TextField(blank=True)
    template_name = models.CharField(max_length=800,default="default")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    def save(self, **kwargs):
        slug_str = f"{ self.person1 } { self.person2 }"
        unique_slugify(self, slug_str, slug_separator='_')
        super(Weddingevent, self).save(**kwargs)

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


#unique slugify from https://djangosnippets.org/snippets/690/
#author https://djangosnippets.org/users/SmileyChris/
def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value