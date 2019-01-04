from django import forms

class QuestionForm(forms.Form):
    newq = forms.CharField(label='Your question', max_length=100)