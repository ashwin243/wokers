from django.db import models

# Create your models here.
# services/models.py
from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name

class Worker(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='workers/')
    description = models.TextField()
    experience = models.CharField(max_length=50)
    licensed = models.BooleanField(default=True)
    estimates = models.BooleanField(default=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    working_days = models.CharField(max_length=100)
    working_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=20)
    date = models.DateField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"Booking by {self.customer_name} for {self.worker.name}"
