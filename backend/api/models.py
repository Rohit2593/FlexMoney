from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

    BATCH_CHOICES = (
        (1, "6-7 AM"),
        (2, "7-8 AM"),
        (3, "8-9 AM"),
        (4, "5-6 PM"),
    )

    batch = models.IntegerField(choices = BATCH_CHOICES)
    payment = models.OneToOneField('Payment', on_delete = models.RESTRICT)

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    details = models.CharField(max_length = 500)

