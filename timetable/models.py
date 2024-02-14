from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as gtl


class WeekDay(models.TextChoices):
    MONDAY = 'MON', gtl('Monday')
    TUESDAY = 'TUE', gtl('Tuesday')
    WEDNESDAY = 'WED', gtl('Wednesday')
    THURSDAY = 'THU', gtl('Thursday')
    FRIDAY = 'FRI', gtl('Friday')
    SATURDAY = 'SAT', gtl('Saturday')
    SUNDAY = 'SUN', gtl('Sunday')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', symmetrical=False)

    def friends(self):
        return self.friends


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    week_day = models.CharField(max_length=3, choices=WeekDay.choices)
    start_time = models.TimeField('start time')
    end_time = models.TimeField('end time')
    description = models.CharField(max_length=500)

    def id(self):
        return self.id

    def user(self):
        return self.user

    def name(self):
        return self.name

    def week_day(self):
        return self.week_day

    def start_time(self):
        return self.start_time

    def end_time(self):
        return self.end_time

    def description(self):
        return self.description
