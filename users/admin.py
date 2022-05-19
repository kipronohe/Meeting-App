from django.contrib import admin
from .models import Profile, Meeting, Venue, Minutes

admin.site.register(Profile)
admin.site.register(Venue)
admin.site.register(Meeting)
admin.site.register(Minutes)


