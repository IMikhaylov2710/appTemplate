from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    active = models.BooleanField(initial=True)
    isAdmin = models.BooleanField(initial=False)


class Variant(models.Model):

    id = models.AutoField(primary_key=True)
    chromosome = models.CharField(max_length=32)
    position = models.IntegerField()
    consequence = models.CharField(max_length=128)
    gene = models.CharField(max_length=32)
    exonic = models.BooleanField(initial=False)
    depth = models.IntegerField()

class Task(models.Model):
    STARTED = 's'
    ALLOCATING = 'a'
    PENDING = 'p'
    FINISHED = 'f'
    QUIT = 'q'
    taskStatus = {
        STARTED : 'started', 
        ALLOCATING : 'allocating containers', 
        PENDING : 'pending', 
        FINISHED : 'finished', 
        QUIT : 'quitted', 
    }

    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=4, choices=taskStatus)
    changedAt = models.DateTimeField()
