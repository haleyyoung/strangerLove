from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length = 100, null = False)
    lastName = models.CharField(max_length = 100, null = False)
    email = models.EmailField(max_length = 254, null = False)

    def __unicode__(self):
        return self.firstName

class Event(models.Model):
    title = models.CharField(max_length = 200, null = False)
    description = models.TextField(max_length = 5000, null = False)
    date = models.DateTimeField(null = False)
    location = models.TextField(max_length = 5000, null = False)
    numberOfPeopleNeeded = models.PositiveIntegerField(null = True)
    owner = models.ForeignKey(User, related_name='owner')

    def __unicode__(self):
        return self.title

class Attend(models.Model):
    user = models.ForeignKey(User, related_name='attendance')
    event = models.ForeignKey(Event, related_name='participants')

    def __unicode__(self):
        return "%s is going to %s" % (self.user, self.event)