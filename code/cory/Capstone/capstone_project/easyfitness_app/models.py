from django.db import models

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

    def __str__(self):
        return self.workout_name