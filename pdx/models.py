from django.db import models


class Pdx(models.Model):
    """Defines all required and desired info for a PDX model."""

    # required info
    # for more detailed info on each field, refer to the docs
    # patient info
    SEXES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('Not specified', 'Not specified'),
    ]
    ETHNICITY_ASSESSMENT = [
        ('', ''),
        ('Self assessed', 'Self assessed'),
        ('Genetic data', 'Genetic data'),
    ]
    patient_id = models.CharField(max_length=100, unique=True)
    patient_sex = models.CharField(max_length=13, choices=SEXES)
    patient_history = models.TextField(blank=True, null=True)
    patient_ethnicity = models.CharField(blank=True, null=True, max_length=100)
    ethnicity_assessment_method = models.CharField(blank=True, null=True, max_length=13, choices=ETHNICITY_ASSESSMENT)
    initial_diagnosis = models.TextField(blank=True, null=True)
    age_at_initial_diagnosis = models.IntegerField(blank=True, null=True)

    # patient tumor at collection time


    # desired info
