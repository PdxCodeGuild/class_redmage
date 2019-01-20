from django.forms import forms, ModelForm
from easyfitness_app.models import Workout

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ['name']

        