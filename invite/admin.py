from django.contrib import admin

from .models import Weddingevent, Guest,Party
admin.site.register(Weddingevent)
admin.site.register(Party)
admin.site.register(Guest)