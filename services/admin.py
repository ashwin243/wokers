from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Service, Worker, Booking

admin.site.register(Service)
admin.site.register(Worker)
admin.site.register(Booking)
