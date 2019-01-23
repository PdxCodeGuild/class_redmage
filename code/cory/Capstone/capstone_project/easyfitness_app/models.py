from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

class Exercise(models.Model):
    workout_name = models.CharField(max_length=60)
    rating_number = models.CharField(max_length=6)
    rating_name = models.CharField(max_length=60)
    workout_type = models.CharField(max_length=60)
    workout_muscle = models.CharField(max_length=60)
    workout_equipment = models.CharField(max_length=60)
    workout_level = models.CharField(max_length=60)
    workout_img_1 = models.CharField(max_length=200)
    workout_img_2 = models.CharField(max_length=200)
    muscle_group_img = models.CharField(max_length=200)
    instructions = models.TextField()

    def instructions_as_list(self):
        return self.instructions.split('\n')

    def slug(self):
        return slugify(self.workout_name)

    def __str__(self):
        return self.workout_name

class Workout(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']