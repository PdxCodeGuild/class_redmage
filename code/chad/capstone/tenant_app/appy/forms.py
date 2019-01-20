from django import forms
from .models import AppyModel
import datetime
from django.contrib.auth.models import User


choice_yes_no = (('Yes', 'Yes'), ('No', 'No'))


class TenantForm(forms.Form):
    # author = forms.ModelMultipleChoiceField(queryset=AppyModel.objects.all(), required=False)
    first_name = forms.CharField(required=False, label='First Name')
    last_name = forms.CharField(required=False, label='Last Name')
    social_security_number = forms.CharField(required=False, label='Social Security Number')
    drivers_license_number = forms.CharField(required=False, label='Drivers License Number')
    date_of_birth = forms.DateField(required=False, label='Date Of Birth', initial=datetime.datetime.today)
    home_phone = forms.CharField(required=False, label='Home Phone Number')
    cell_phone = forms.CharField(required=False, label='Cell Phone Number')
    email_address = forms.CharField(required=False, label='Email Address', widget=forms.EmailInput)

    current_address = forms.CharField(required=False, label='Current Address Line 1')
    current_address_line_2 = forms.CharField(required=False, label='Current Address Line 2')
    current_city = forms.CharField(required=False, label=' Current City')
    current_state_abv = forms.CharField(required=False, label='Current State Abbreviation')
    current_zip = forms.CharField(required=False, label=' Current Zip')

    previous_address = forms.CharField(required=False, label='Previous Address Line 1')
    previous_address_line_2 = forms.CharField(required=False, label='Previous Address Line 2')
    previous_city = forms.CharField(required=False, label='Previous City')
    previous_state_abv = forms.CharField(required=False, label='Previous State Abbreviation')
    previous_zip = forms.CharField(required=False, label='Previous Zip')

    current_employer_name = forms.CharField(required=False, label='Current Employer Name')
    current_employer_address = forms.CharField(required=False, label='Current Employer Address Line 1')
    current_employer_address_line_2 = forms.CharField(required=False, label='Current Employer Address Line 2')
    current_employer_state_abv = forms.CharField(required=False, label='Current Employer State')
    current_employer_zip = forms.CharField(required=False, label='Current Employer Zip')
    current_employer_phone = forms.CharField(required=False, label='Current Employer Phone')
    current_employer_start_date = forms.DateField(required=False, initial=datetime.date.today,
                                                  label='Current Employer Start Date',
                                                  widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    current_employer_end_date = forms.DateField(required=False, initial=datetime.datetime.today,
                                                label='Current Employer End Date',
                                                widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    current_employer_may_contact = forms.BooleanField(required=False, label='Current Employer May We Contact?')

    previous_employer_name = forms.CharField(required=False, label='Previous Employer Name')
    previous_employer_address = forms.CharField(required=False, label='Previous Employer Address Line 1')
    previous_employer_address_line_2 = forms.CharField(required=False, label='Previous Employer Address Line 2')
    previous_employer_state_abv = forms.CharField(required=False, label='Previous Employer State Abbreviation')
    previous_employer_zip = forms.CharField(required=False, label='Previous Employer Zip')
    previous_employer_phone = forms.CharField(required=False, label='Previous Employer Phone')
    previous_employer_start_date = forms.DateField(required=False, initial=datetime.datetime.today,
                                                   label='Previous Employer Start Date',
                                                   widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    previous_employer_end_date = forms.DateField(required=False, initial=datetime.datetime.today,
                                                 label='Previous Employer End Date',
                                                 widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    previous_employer_may_contact = forms.BooleanField(required=False, label='Previous Employer May We Contact?')

    additional_person_1 = forms.CharField(required=False, label='Addition Person #1')
    additional_person_2 = forms.CharField(required=False, label='Addition Person #2')
    additional_person_3 = forms.CharField(required=False, label='Addition Person #3')
    additional_person_4 = forms.CharField(required=False, label='Addition Person #4')

    add_question_full_deposit = forms.BooleanField(required=False, label='Will You Have The Full Deposit If Accepted?',
                                                   widget=forms.RadioSelect(choices=choice_yes_no))
    add_question_felony = forms.BooleanField(required=False, label='Have You Ever Been Convicted Of A Felony?')
    add_question_felony_explain = forms.CharField(required=False, label='Explain Felony:',
                                                  widget=forms.Textarea(attrs={'cols': 100}))
    add_question_dogs = forms.IntegerField(required=False, initial=1, label='How Many Dogs?')
    add_question_cats = forms.IntegerField(required=False, initial=1, label='How Many Cats?')
    add_question_water_filled_furniture = forms.BooleanField(required=False,
                                                             label='Do You Have Any Water Filled Furniture')
    add_question_ever_evicted = forms.BooleanField(required=False, label='Have You Ever Ben Evicted?')
    add_question_ever_evicted_explain = forms.CharField(required=False, label='Explain Eviction:',
                                                        widget=forms.Textarea(attrs={'cols': 100}))
    add_question_judgements = forms.BooleanField(required=False, label='Do You Have Any Judgements Against You?')
    add_question_judgements_explain = forms.CharField(required=False, label='Explain Judgements:',
                                                      widget=forms.Textarea(attrs={'cols': 100}))
    add_question_collections = forms.BooleanField(required=False, label='Do You Have Any Collections?')
    add_question_collections_explain = forms.CharField(required=False, label='Explain Collections:',
                                                       widget=forms.Textarea(attrs={'cols': 100}))


    # def clean_first_name(self, *args, **kwargs):
    #     first_name = self.cleaned_data.get('first_name')
    #     if not first_name.isalpha():
    #         raise forms.ValidationError("Your Name Contains Invalid Characters")
    #
    # def clean_last_name(self):
    #     last_name = self.cleaned_data.get('last_name')
    #     if not last_name.isalpha():
    #         raise forms.ValidationError("Your Name Contains Invalid Characters")

    # def clean_social_security_number(self):
    #     pass
    #
    # def clean_drivers_license_number(self):
    #     pass
    #
    # def clean_date_of_birth(self):
    #     pass
    #
    # def clean_home_phone(self):
    #     pass
    #
    # def clean_cell_phone(self):
    #     pass
    #
    # def clean_email_address(self):
    #     pass
    #
    # def clean_current_address(self):
    #     pass
    #
    # def clean_current_address_line_2(self):
    #     pass
    #
    # def clean_current_city(self):
    #     pass
    #
    # def clean_current_state_abv(self):
    #     pass
    #
    # def clean_current_zip(self):
    #     pass
    #
    # def clean_previous_address(self):
    #     pass
    #
    # def clean_previous_address_line_2(self):
    #     pass
    #
    # def clean_previous_city(self):
    #     pass
    #
    # def clean_previous_state_abv(self):
    #     pass
    #
    # def clean_previous_zip(self):
    #     pass
    #
    # def clean_current_employer_name(self):
    #     pass
    #
    # def clean_current_employer_address(self):
    #     pass
    #
    # def clean_current_employer_address_line_2(self):
    #     pass
    #
    # def clean_current_employer_state_abv(self):
    #     pass
    #
    # def clean_current_employer_zip(self):
    #     pass
    #
    # def clean_current_employer_phone(self):
    #     pass
    #
    # def clean_current_employer_start_date(self):
    #     pass
    #
    # def clean_current_employer_end_date(self):
    #     pass
    #
    # def clean_current_employer_may_contact(self):
    #     pass
    #
    # def clean_previous_employer_name(self):
    #     pass
    #
    # def clean_previous_employer_address(self):
    #     pass
    #
    # def clean_previous_employer_address_line_2(self):
    #     pass
    #
    # def clean_previous_employer_state_abv(self):
    #     pass
    #
    # def clean_previous_employer_zip(self):
    #     pass
    #
    # def clean_previous_employer_phone(self):
    #     pass
    #
    # def clean_previous_employer_start_date(self):
    #     pass
    #
    # def clean_previous_employer_end_date(self):
    #     pass
    #
    # def clean_previous_employer_may_contact(self):
    #     pass
    #
    # def clean_additional_person_1(self):
    #     pass
    #
    # def clean_additional_person_2(self):
    #     pass
    #
    # def clean_additional_person_3(self):
    #     pass
    #
    # def clean_additional_person_4(self):
    #     pass
    #
    # def clean_add_question_full_deposit(self):
    #     pass
    #
    # def clean_add_question_felony(self):
    #     pass
    #
    # def clean_add_question_felony_explain(self):
    #     pass
    #
    # def clean_add_question_dogs(self):
    #     pass
    #
    # def clean_add_question_cats(self):
    #     pass
    #
    # def clean_add_question_water_filled_furniture(self):
    #     pass
    #
    # def clean_add_question_ever_evicted(self):
    #     pass
    #
    # def clean_add_question_ever_evicted_explain(self):
    #     pass
    #
    # def clean_add_question_judgements(self):
    #     pass
    #
    # def clean_add_question_judgements_explain(self):
    #     pass
    #
    # def clean_add_question_collections(self):
    #     pass
    #
    # def clean_add_question_collections_explain(self):
    #     pass
