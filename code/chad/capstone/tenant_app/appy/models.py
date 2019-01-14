from django.db import models



class AppyModel(models.Model):
    date_time_form_filled = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(null=False, blank=False, max_length=20)
    last_name = models.CharField(null=False, blank=False, max_length=20)
    social_security_number = models.CharField(null=False, blank=False, max_length=9)
    drivers_license_number = models.CharField(null=False, blank=False, max_length=20)
    date_of_birth = models.DateField(null=False, blank=False)
    home_phone = models.CharField(null=False, blank=False, max_length=10)
    cell_phone = models.CharField(null=False, blank=False, max_length=10)
    email_address = models.CharField(null=False, blank=False, max_length=20)

    current_address = models.CharField(null=False, blank=False, max_length=100)
    current_address_line_2 = models.CharField(null=False, blank=False, max_length=100)
    current_city = models.CharField(null=False, blank=False, max_length=20)
    current_state_abv = models.CharField(null=False, blank=False, max_length=2)
    current_zip = models.CharField(null=False, blank=False, max_length=5)

    previous_address = models.CharField(null=False, blank=False, max_length=100)
    previous_address_line_2 = models.CharField(null=False, blank=False, max_length=100)
    previous_city = models.CharField(null=False, blank=False, max_length=20)
    previous_state = models.CharField(null=False, blank=False, max_length=2)
    previous_zip = models.CharField(null=False, blank=False, max_length=5)

    current_employer_name = models.CharField(null=False, blank=False, max_length=75)
    current_employer_address = models.CharField(null=False, blank=False, max_length=100)
    current_employer_address_line_2 = models.CharField(null=False, blank=False, max_length=100)
    current_employer_state_abv = models.CharField(null=False, blank=False, max_length=2)
    current_employer_zip = models.CharField(null=False, blank=False, max_length=5)
    current_employer_phone = models.CharField(null=False, blank=False, max_length=10)
    current_employer_start_date = models.DateField(null=False, blank=False)
    current_employer_end_date = models.DateField(null=False, blank=False)
    current_employer_may_contact = models.BooleanField(null=False, blank=False)

    previous_employer_name = models.CharField(null=False, blank=False, max_length=75)
    previous_employer_address = models.CharField(null=False, blank=False, max_length=100)
    previous_employer_address_line_2 = models.CharField(null=False, blank=False, max_length=100)
    previous_employer_state_abv = models.CharField(null=False, blank=False, max_length=2)
    previous_employer_zip = models.CharField(null=False, blank=False, max_length=5)
    previous_employer_phone = models.CharField(null=False, blank=False, max_length=75)
    previous_employer_start_date = models.DateField(null=False, blank=False)
    previous_employer_end_date = models.DateField(null=False, blank=False)
    previous_employer_may_contact = models.BooleanField(null=False, blank=False)

    additional_person_1 = models.CharField(null=False, blank=False, max_length=15)
    additional_person_2 = models.CharField(null=False, blank=False, max_length=15)
    additional_person_3 = models.CharField(null=False, blank=False, max_length=15)
    additional_person_4 = models.CharField(null=False, blank=False, max_length=15)

    add_question_full_deposit = models.BooleanField(null=False, blank=False)
    add_question_felony = models.BooleanField(null=False, blank=False)
    add_question_felony_explain = models.CharField(null=False, blank=False, max_length=500)
    add_question_dogs = models.IntegerField(null=False, blank=False)
    add_question_cats = models.IntegerField(null=False, blank=False)
    add_question_water_filled_furniture = models.BooleanField(null=False, blank=False)
    add_question_ever_evicted = models.BooleanField(null=False, blank=False)
    add_question_ever_evicted_explain = models.CharField(null=False, blank=False, max_length=500)
    add_question_judgements = models.BooleanField(null=False, blank=False)
    add_question_judgements_explain = models.CharField(null=False, blank=False, max_length=500)
    add_question_collections = models.BooleanField(null=False, blank=False)
    add_question_collections_explain = models.CharField(null=False, blank=False, max_length=500)


