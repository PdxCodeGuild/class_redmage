from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class AppyModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_time_form_filled = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    social_security_number = models.CharField(max_length=9)
    drivers_license_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    home_phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=10)
    email_address = models.CharField(max_length=20)

    current_address = models.CharField(max_length=100)
    current_address_line_2 = models.CharField(max_length=100)
    current_city = models.CharField(max_length=20)
    current_state_abv = models.CharField(max_length=2)
    current_zip = models.CharField(max_length=5)

    previous_address = models.CharField(max_length=100)
    previous_address_line_2 = models.CharField(max_length=100)
    previous_city = models.CharField(max_length=20)
    previous_state_abv = models.CharField(max_length=2)
    previous_zip = models.CharField(max_length=5)

    current_employer_name = models.CharField(max_length=75)
    current_employer_address = models.CharField(max_length=100)
    current_employer_address_line_2 = models.CharField(max_length=100)
    current_employer_state_abv = models.CharField(max_length=2)
    current_employer_zip = models.CharField(max_length=5)
    current_employer_phone = models.CharField(max_length=10)
    current_employer_start_date = models.DateField()
    current_employer_end_date = models.DateField()
    current_employer_may_contact = models.BooleanField()

    previous_employer_name = models.CharField(max_length=75)
    previous_employer_address = models.CharField(max_length=100)
    previous_employer_address_line_2 = models.CharField(max_length=100)
    previous_employer_state_abv = models.CharField(max_length=2)
    previous_employer_zip = models.CharField(max_length=5)
    previous_employer_phone = models.CharField(max_length=75)
    previous_employer_start_date = models.DateField()
    previous_employer_end_date = models.DateField()
    previous_employer_may_contact = models.BooleanField()

    additional_person_1 = models.CharField(max_length=15)
    additional_person_2 = models.CharField(max_length=15)
    additional_person_3 = models.CharField(max_length=15)
    additional_person_4 = models.CharField(max_length=15)

    add_question_full_deposit = models.BooleanField()
    add_question_felony = models.BooleanField()
    add_question_felony_explain = models.CharField(max_length=500)
    add_question_dogs = models.IntegerField()
    add_question_cats = models.IntegerField()
    add_question_water_filled_furniture = models.BooleanField()
    add_question_ever_evicted = models.BooleanField()
    add_question_ever_evicted_explain = models.CharField(max_length=500)
    add_question_judgements = models.BooleanField()
    add_question_judgements_explain = models.CharField(max_length=500)
    add_question_collections = models.BooleanField()
    add_question_collections_explain = models.CharField(max_length=500)

    # def __str__(self):
    #     return self.first_name
    #
    # def get_absolute_url(self):
    #     return reverse('tenant_from_edit', kwargs={'pk': self.pk})


class MaintyModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_time_form_filled = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    problem_description = models.CharField(max_length=1000)
