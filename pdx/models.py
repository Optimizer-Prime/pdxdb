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
    age_at_initial_diagnosis = models.PositiveIntegerField(blank=True, null=True)

    # patient tumor at collection time
    SHAREABLE = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    TREATED_OPTIONS = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Not specified', 'Not specified'),
    ]
    sample_id = models.CharField(max_length=250, unique=True)
    collection_date = models.DateField(blank=True, null=True)
    collection_event = models.CharField(blank=True, null=True, max_length=250)
    months_since_collection_one = models.PositiveIntegerField(blank=True, null=True)
    age_in_years_at_collection = models.PositiveIntegerField()
    diagnosis = models.TextField()
    diagnosis_notes = models.TextField(blank=True, null=True)
    tumor_type = models.CharField(max_length=100)
    primary_site = models.CharField(max_length=250)
    collection_site = models.CharField(max_length=250)
    stage = models.CharField(blank=True, null=True, max_length=30)
    staging_system = models.CharField(blank=True, null=True, max_length=250)
    grade = models.CharField(blank=True, null=True, max_length=30)
    grading_system = models.CharField(blank=True, null=True, max_length=250)
    virology_status = models.TextField(blank=True, null=True)
    share_status = models.CharField(max_length=3, choices=SHAREABLE)
    treatment_naive_at_collection = models.CharField(blank=True, null=True, max_length=100)
    treated = models.CharField(blank=True, null=True, max_length=13, choices=TREATED_OPTIONS)
    prior_treatment = models.CharField(blank=True, null=True, max_length=13, choices=TREATED_OPTIONS)
    model_id = models.CharField(max_length=100, unique=True)

    # PDX model details


    # desired info
