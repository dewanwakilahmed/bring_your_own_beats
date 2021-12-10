import uuid
from django.db import models

# Create your models here.


class tournaments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    max_contestant = models.IntegerField
    buy_in_count = models.IntegerField

    class Meta:
        abstract = True


class contestants_of_one_vs_one(tournaments):
    contestant_one = models.CharField(max_length=100)
    contestant_two = models.CharField(max_length=100)


class contestants_of_four_producer(tournaments):
    contestant_one = models.CharField(max_length=100)
    contestant_two = models.CharField(max_length=100)
    contestant_three = models.CharField(max_length=100)
    contestant_four = models.CharField(max_length=100)


class contestants_of_eight_producer(tournaments):
    contestant_one = models.CharField(max_length=100)
    contestant_two = models.CharField(max_length=100)
    contestant_three = models.CharField(max_length=100)
    contestant_four = models.CharField(max_length=100)
    contestant_five = models.CharField(max_length=100)
    contestant_six = models.CharField(max_length=100)
    contestant_seven = models.CharField(max_length=100)
    contestant_eight = models.CharField(max_length=100)
