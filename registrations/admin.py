from django.contrib import admin
from .models import Registration, Participant, Certification

# Register your models here.
admin.site.register(Registration)
admin.site.register(Participant)
admin.site.register(Certification)
