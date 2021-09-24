import datetime
import random
import string

import pytz
from django.test import TestCase


import factory
import factory.fuzzy

from invite.models import Party, Guest, Weddingevent


class WeddingFactory(factory.django.DjangoModelFactory):
    person1 = factory.fuzzy.FuzzyText(),
    person2 = factory.fuzzy.FuzzyText(),
    greeting = factory.fuzzy.FuzzyText(),
    blurb = factory.fuzzy.FuzzyText(),
    body = factory.fuzzy.FuzzyText(),
    location = factory.fuzzy.FuzzyText(),
    meetingURL = factory.fuzzy.FuzzyText(),
    time_and_date = datetime.datetime(2023, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
    notepad = factory.fuzzy.FuzzyText(),
    template_name = "default",
    body = factory.Faker(
        'paragraph', nb_sentences=3,
        variable_nb_sentences=True
    )

    class Meta:
        model = Weddingevent


class WeddingTest(TestCase):
    def setUp(self):
        self.wedding = Weddingevent.objects.create(
        person1 = "Adele Smith",
        person2 = "Ronnie Baltimore",
        greeting = "Welcome to our wedding!",
        blurb = "We're the best couple ever. Believe it!",
        body = "blah blah, its gonna be at the steakhouse, you gonna love it",
        location = "Steakhouse USA",
        meetingURL = "Zoom.com/potato",
        time_and_date = datetime.datetime(2023, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
        notepad = "",
        template_name = "default",
        )

        self.party = Party.objects.create(
        wedding = self.wedding,
        invite_code_short = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
        name = "Texas Family",
        category = "Weirdoes",
        comments = "They eat soup with forks",
        email = "1@1.com",
        phone = "12121212212",
        )

        self.guest1 = Guest.objects.create(
            party=self.party,
            first_name='Ned',
            last_name='Stark',
            email = "2@2.com",
            phone = "121212121212",
            kosher_meal = True,
            is_child = False,
        )
        self.guest2 = Guest.objects.create(
            party=self.party,
            first_name='Catelyn',
            last_name='Stark',
            email="2@2.com",
            phone="121212121212",
            kosher_meal=True,
            is_child=False,
        )

    def tearDown(self):
        Party.objects.all().delete()

    def test_any_guests_attending_default(self):
        self.assertFalse(self.party.any_guests_attending)

    def test_any_guests_attending_false(self):
        self.guest1.is_attending = False
        self.guest1.save()
        self.guest2.is_attending = False
        self.guest2.save()
        self.assertFalse(self.party.any_guests_attending)

    def test_any_guests_attending_true(self):
        self.guest1.is_attending = False
        self.guest1.save()
        self.guest2.is_attending = True
        self.guest2.save()
        self.assertTrue(self.party.any_guests_attending)


