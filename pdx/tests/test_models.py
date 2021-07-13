from django.test import TestCase
from pdx.models import Pdx

SEXES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('not specified', 'Not specified'),
    ]
ETHNICITY_ASSESSMENT = [
    ('self assessed', 'Self assessed'),
    ('genetic data', 'Genetic data'),
]
SHAREABLE = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
TREATMENT_NAIVE = [
    ('naive', 'Treatment naive'),
    ('not naive', 'Not treatment naive'),
    ('not specified', 'Not specified'),
]
TREATED_OPTIONS = [
    ('Y', 'Yes'),
    ('N', 'No'),
    ('unknown', 'Unknown'),
]
ACCESS_MODALITY = [
        ('transnational', 'Transnational access'),
        ('collaboration', 'Collaboration only'),
]


class PdxModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Pdx.objects.create(patient_id='A08593', patient_sex='M', patient_history='has breast cancer',
                           patient_ethnicity='ethnicity', ethnicity_assessment_method='self assessed',
                           initial_diagnosis='ductal carcinoma', age_at_initial_diagnosis=45,
                           sample_id='A08593_01', collection_date='2021-03-13', collection_event='collection 1',
                           months_since_collection_one=3, age_in_years_at_collection=40, diagnosis='Cancer',
                           diagnosis_notes='sample sent to lab', tumor_type='primary', primary_site='breast',
                           collection_site='right breast', stage='T1', staging_system='TNM',
                           grade='2', grading_system='standard', virology_status='human papillomavirus',
                           treatment_info_shareable='Y', treatment_naive_at_collection='naive',
                           treated='Y', prior_treatment='Y', model_id='ABC_001',
                           host_strain='host strain', host_strain_full='host strain full',
                           engraftment_site='fat pad', engraftment_type='orthotopic',
                           sample_type='tissue fragment', sample_state='fresh', passage_number='0, 1',
                           publications='none', validation_techniques='DNA auth', validation_description='high',
                           passages_validated='0, 1', validation_host_strain_full='full strain',
                           provider_type='academia', model_accessibility='both',
                           europdx_access_modality='transnational', contact_email='test@email.com',
                           contact_name='name', provider_name='university',
                           provider_abbreviation='SU', project_name='PDX project', )

    def return_test_data(self):
        pdx = Pdx.objects.get(model_id='ABC_001')
        return pdx

    def test_patient_id_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('patient_id').verbose_name
        self.assertEqual(field_label, 'patient id')

    def test_patient_id_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('patient_id').max_length
        self.assertEqual(max_length, 200)

    def test_patient_sex_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('patient_sex').verbose_name
        self.assertEqual(field_label, 'patient sex')

    def test_patient_sex_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('patient_sex').max_length
        self.assertEqual(max_length, 13)

    def test_patient_sex_choices(self):
        choices = PdxModelTest.return_test_data(self)._meta.get_field('patient_sex').choices
        self.assertEqual(choices, SEXES)

    def test_patient_history_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('patient_history').verbose_name
        self.assertEqual(field_label, 'patient history')

    def test_patient_ethnicity_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('patient_ethnicity').verbose_name
        self.assertEqual(field_label, 'patient ethnicity')

    def test_patient_ethnicity_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('patient_ethnicity').max_length
        self.assertEqual(max_length, 100)

    def test_ethnicity_assessment_method_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('ethnicity_assessment_method').verbose_name
        self.assertEqual(field_label, 'ethnicity assessment method')

    def test_ethnicity_assessment_method_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('ethnicity_assessment_method').max_length
        self.assertEqual(max_length, 13)

    def test_ethnicity_assessment_method_choices(self):
        choices = PdxModelTest.return_test_data(self)._meta.get_field('ethnicity_assessment_method').choices
        self.assertEqual(choices, ETHNICITY_ASSESSMENT)

    def test_initial_diagnosis_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('initial_diagnosis').verbose_name
        self.assertEqual(field_label, 'initial diagnosis')

    def test_age_at_initial_diagnosis_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('age_at_initial_diagnosis').verbose_name
        self.assertEqual(field_label, 'age at initial diagnosis')

    def test_sample_id_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('sample_id').verbose_name
        self.assertEqual(field_label, 'sample id')

    def test_sample_id_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('sample_id').max_length
        self.assertEqual(max_length, 250)

    def test_collection_date_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('collection_date').verbose_name
        self.assertEqual(field_label, 'collection date')

    def test_collection_event_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('collection_event').verbose_name
        self.assertEqual(field_label, 'collection event')

    def test_collection_event_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('collection_event').max_length
        self.assertEqual(max_length, 250)

    def test_months_since_collection_one_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('months_since_collection_one').verbose_name
        self.assertEqual(field_label, 'months since collection one')

    def test_age_in_years_at_collection_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('age_in_years_at_collection').verbose_name
        self.assertEqual(field_label, 'age in years at collection')

    def test_diagnosis_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('diagnosis').verbose_name
        self.assertEqual(field_label, 'diagnosis')

    def test_diagnosis_notes_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('diagnosis_notes').verbose_name
        self.assertEqual(field_label, 'diagnosis notes')

    def test_tumor_type_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('tumor_type').verbose_name
        self.assertEqual(field_label, 'tumor type')

    def test_tumor_type_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('tumor_type').max_length
        self.assertEqual(max_length, 100)

    def test_primary_site_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('primary_site').verbose_name
        self.assertEqual(field_label, 'primary site')

    def test_primary_site_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('primary_site').max_length
        self.assertEqual(max_length, 250)

    def test_collection_site_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('collection_site').verbose_name
        self.assertEqual(field_label, 'collection site')

    def test_collection_site_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('collection_site').max_length
        self.assertEqual(max_length, 250)

    def test_stage_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('stage').verbose_name
        self.assertEqual(field_label, 'stage')

    def test_stage_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('stage').max_length
        self.assertEqual(max_length, 30)

    def test_staging_system_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('staging_system').verbose_name
        self.assertEqual(field_label, 'staging system')

    def test_staging_system_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('staging_system').max_length
        self.assertEqual(max_length, 250)

    def test_grade_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('grade').verbose_name
        self.assertEqual(field_label, 'grade')

    def test_grade_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('grade').max_length
        self.assertEqual(max_length, 30)

    def test_grading_system_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('grading_system').verbose_name
        self.assertEqual(field_label, 'grading system')

    def test_grading_system_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('grading_system').max_length
        self.assertEqual(max_length, 250)

    def test_virology_status_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('virology_status').verbose_name
        self.assertEqual(field_label, 'virology status')

    def test_treatment_info_shareable_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('treatment_info_shareable').verbose_name
        self.assertEqual(field_label, 'treatment info shareable')

    def test_treatment_info_shareable_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('treatment_info_shareable').max_length
        self.assertEqual(max_length, 3)

    def test_treatment_info_shareable_choices(self):
        choices = PdxModelTest.return_test_data(self)._meta.get_field('treatment_info_shareable').choices
        self.assertEqual(choices, SHAREABLE)

    def test_treatment_naive_at_collection_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('treatment_naive_at_collection').verbose_name
        self.assertEqual(field_label, 'treatment naive at collection')

    def test_treatment_naive_at_collection_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('treatment_naive_at_collection').max_length
        self.assertEqual(max_length, 13)

    def test_treatment_naive_at_collection_choices(self):
        choices = PdxModelTest.return_test_data(self)._meta.get_field('treatment_naive_at_collection').choices
        self.assertEqual(choices, TREATMENT_NAIVE)

    def test_treated_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('treated').verbose_name
        self.assertEqual(field_label, 'treated')

    def test_treated_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('treated').max_length
        self.assertEqual(max_length, 13)

    def test_treated_choices(self):
        choices = PdxModelTest.return_test_data(self)._meta.get_field('treated').choices
        self.assertEqual(choices, TREATED_OPTIONS)

    def test_prior_treatment_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('prior_treatment').verbose_name
        self.assertEqual(field_label, 'prior treatment')

    def test_prior_treatment_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('prior_treatment').max_length
        self.assertEqual(max_length, 13)

    def test_prior_treatment_choices(self):
        choices = PdxModelTest.return_test_data(self)._meta.get_field('prior_treatment').choices
        self.assertEqual(choices, TREATED_OPTIONS)

    def test_model_id_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('model_id').verbose_name
        self.assertEqual(field_label, 'model id')

    def test_model_id_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('model_id').max_length
        self.assertEqual(max_length, 100)

    def test_model_id_unique(self):
        unique = PdxModelTest.return_test_data(self)._meta.get_field('model_id').unique
        self.assertTrue(unique)

    def test_host_strain_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('host_strain').verbose_name
        self.assertEqual(field_label, 'host strain')

    def test_host_strain_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('host_strain').max_length
        self.assertEqual(max_length, 250)

    def test_host_strain_full_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('host_strain_full').verbose_name
        self.assertEqual(field_label, 'host strain full')

    def test_engraftment_site_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('engraftment_site').verbose_name
        self.assertEqual(field_label, 'engraftment site')

    def test_engraftment_site_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('engraftment_site').max_length
        self.assertEqual(max_length, 250)

    def test_engraftment_type_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('engraftment_type').verbose_name
        self.assertEqual(field_label, 'engraftment type')

    def test_engraftment_type_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('engraftment_type').max_length
        self.assertEqual(max_length, 250)

    def test_sample_type_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('sample_type').verbose_name
        self.assertEqual(field_label, 'sample type')

    def test_sample_type_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('sample_type').max_length
        self.assertEqual(max_length, 250)

    def test_sample_state_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('sample_state').verbose_name
        self.assertEqual(field_label, 'sample state')

    def test_sample_state_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('sample_state').max_length
        self.assertEqual(max_length, 250)

    def test_passage_number_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('passage_number').verbose_name
        self.assertEqual(field_label, 'passage number')

    def test_passage_number_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('passage_number').max_length
        self.assertEqual(max_length, 250)

    def test_publications_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('publications').verbose_name
        self.assertEqual(field_label, 'publications')

    def test_validation_techniques_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('validation_techniques').verbose_name
        self.assertEqual(field_label, 'validation techniques')

    def test_validation_description_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('validation_description').verbose_name
        self.assertEqual(field_label, 'validation description')

    def test_passages_validated_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('passages_validated').verbose_name
        self.assertEqual(field_label, 'passages validated')

    def test_passages_validated_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('passages_validated').max_length
        self.assertEqual(max_length, 250)

    def test_validation_host_strain_full_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('validation_host_strain_full').verbose_name
        self.assertEqual(field_label, 'validation host strain full')

    def test_provider_type_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('provider_type').verbose_name
        self.assertEqual(field_label, 'provider type')

    def test_provider_type_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('provider_type').max_length
        self.assertEqual(max_length, 250)

    def test_model_accessibility_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('model_accessibility').verbose_name
        self.assertEqual(field_label, 'model accessibility')

    def test_model_accessibility_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('model_accessibility').max_length
        self.assertEqual(max_length, 250)

    def test_europdx_access_modality_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('europdx_access_modality').verbose_name
        self.assertEqual(field_label, 'europdx access modality')

    def test_europdx_access_modality_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('europdx_access_modality').max_length
        self.assertEqual(max_length, 20)

    def test_europdx_access_modality_choices(self):
        choices = PdxModelTest.return_test_data(self)._meta.get_field('europdx_access_modality').choices
        self.assertEqual(choices, ACCESS_MODALITY)

    def test_contact_email_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('contact_email').verbose_name
        self.assertEqual(field_label, 'contact email')

    def test_contact_name_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('contact_name').verbose_name
        self.assertEqual(field_label, 'contact name')

    def test_contact_name_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('contact_name').max_length
        self.assertEqual(max_length, 50)

    def test_provider_name_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('provider_name').verbose_name
        self.assertEqual(field_label, 'provider name')

    def test_provider_name_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('provider_name').max_length
        self.assertEqual(max_length, 50)

    def test_provider_abbreviation_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('provider_abbreviation').verbose_name
        self.assertEqual(field_label, 'provider abbreviation')

    def test_provider_abbreviation_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('provider_abbreviation').max_length
        self.assertEqual(max_length, 10)

    def test_project_name_label(self):
        field_label = PdxModelTest.return_test_data(self)._meta.get_field('project_name').verbose_name
        self.assertEqual(field_label, 'project name')

    def test_project_name_max_length(self):
        max_length = PdxModelTest.return_test_data(self)._meta.get_field('project_name').max_length
        self.assertEqual(max_length, 100)
