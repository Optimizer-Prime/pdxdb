from django.test import SimpleTestCase

from pdx.forms import PdxForm

UNIQUE = 'Must be unique.'
STRAIN_LOOKUP = "Look up <a href='http://www.informatics.jax.org/home/strain' " \
                "target='_blank' rel='noopener noreferrer'>here.</a>"
PASSAGES_HELP_TEXT = 'Comma seperated list of passage numbers.'
COLLECTION_EVENT_HELP_TEXT = 'If collection date entered, leave blank.'
VALIDATION_TECHNIQUES_HELP_TEXT = 'List all that apply. Separate with comma.'
VALIDATION_DESCRIPTION_HELP_TEXT = 'Must be clear if model is validated or not.'
VIROLOGY_STATUS_HELP_TEXT = 'List all viruses the patient tested positive for. Provide full name. Separate with comma.'


class PdxFormTest(SimpleTestCase):

    def test_patient_id_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['patient_id'].label is None
                        or form.fields['patient_id'].label == 'Patient id')

    def test_patient_sex_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['patient_sex'].label is None
                        or form.fields['patient_sex'].label == 'Patient sex')

    def test_patient_ethnicity_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['patient_ethnicity'].label is None
                        or form.fields['patient_ethnicity'].label == 'Patient ethnicity')

    def test_ethnicity_assessment_method_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['ethnicity_assessment_method'].label is None
                        or form.fields['ethnicity_assessment_method'].label == 'Ethnicity assessment method')

    def test_age_at_initial_diagnosis_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['age_at_initial_diagnosis'].label is None
                        or form.fields['age_at_initial_diagnosis'].label == 'Age at initial diagnosis')

    def test_patient_history_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['patient_history'].label is None
                        or form.fields['patient_history'].label == 'Patient history')

    def test_initial_diagnosis_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['initial_diagnosis'].label is None
                        or form.fields['initial_diagnosis'].label == 'Initial diagnosis')

    def test_sample_id_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['sample_id'].label is None
                        or form.fields['sample_id'].label == 'Sample id')

    def test_sample_id_help_text(self):
        form = PdxForm()
        self.assertEqual(form.fields['sample_id'].help_text, UNIQUE)

    def test_collection_date_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['collection_date'].label is None
                        or form.fields['collection_date'].label == 'Collection date')

    def test_collection_event_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['collection_event'].label is None
                        or form.fields['collection_event'].label == 'Collection event')

    def test_collection_event_help_text(self):
        form = PdxForm()
        self.assertTrue(form.fields['collection_event'].help_text is None
                        or form.fields['collection_event'].help_text == COLLECTION_EVENT_HELP_TEXT)

    def test_months_since_collection_one_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['months_since_collection_one'].label is None
                        or form.fields['months_since_collection_one'].label == 'Months since collection one')

    def test_diagnosis_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['diagnosis'].label is None
                        or form.fields['diagnosis'].label == 'Diagnosis')

    def test_diagnosis_notes_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['diagnosis_notes'].label is None
                        or form.fields['diagnosis_notes'].label == 'Diagnosis notes')

    def test_age_in_years_at_collection_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['age_in_years_at_collection'].label is None
                        or form.fields['age_in_years_at_collection'].label == 'Age in years at collection')

    def test_tumor_type_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['tumor_type'].label is None
                        or form.fields['tumor_type'].label == 'Tumor type')

    def test_primary_site_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['primary_site'].label is None
                        or form.fields['primary_site'].label == 'Primary site')

    def test_collection_site_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['collection_site'].label is None
                        or form.fields['collection_site'].label == 'Collection site')

    def test_stage_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['stage'].label is None
                        or form.fields['stage'].label == 'Stage')

    def test_staging_system_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['staging_system'].label is None
                        or form.fields['staging_system'].label == 'Staging system')

    def test_grade_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['grade'].label is None
                        or form.fields['grade'].label == 'Grade')

    def test_grading_system_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['grading_system'].label is None
                        or form.fields['grading_system'].label == 'Grading system')

    def test_treatment_info_shareable_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['treatment_info_shareable'].label is None
                        or form.fields['treatment_info_shareable'].label == 'Treatment info shareable')

    def test_treatment_naive_at_collection_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['treatment_naive_at_collection'].label is None
                        or form.fields['treatment_naive_at_collection'].label == 'Treatment naive at collection')

    def test_treated_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['treated'].label is None
                        or form.fields['treated'].label == 'Treated')

    def test_prior_treatment_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['prior_treatment'].label is None
                        or form.fields['prior_treatment'].label == 'Prior treatment')

    def test_virology_status_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['virology_status'].label is None
                        or form.fields['virology_status'].label == 'Virology status')

    def test_virology_status_help_text(self):
        form = PdxForm()
        self.assertEqual(form.fields['virology_status'].help_text, VIROLOGY_STATUS_HELP_TEXT)

    def test_model_id_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['model_id'].label is None
                        or form.fields['model_id'].label == 'Model id')

    def test_model_id_help_text(self):
        form = PdxForm()
        self.assertEqual(form.fields['model_id'].help_text, UNIQUE)

    def test_host_strain_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['host_strain'].label is None
                        or form.fields['host_strain'].label == 'Host strain')

    def test_host_strain_full_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['host_strain_full'].label is None
                        or form.fields['host_strain_full'].label == 'Host strain full')

    def test_host_strain_full_help_text(self):
        form = PdxForm()
        self.assertEqual(form.fields['host_strain_full'].help_text, STRAIN_LOOKUP)

    def test_engraftment_site_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['engraftment_site'].label is None
                        or form.fields['engraftment_site'].label == 'Engraftment site')

    def test_engraftment_type_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['engraftment_type'].label is None
                        or form.fields['engraftment_type'].label == 'Engraftment type')

    def test_sample_type_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['sample_type'].label is None
                        or form.fields['sample_type'].label == 'Sample type')

    def test_sample_state_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['sample_state'].label is None
                        or form.fields['sample_state'].label == 'Sample state')

    def test_passage_number_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['passage_number'].label is None
                        or form.fields['passage_number'].label == 'Passage number')

    def test_passage_number_help_text(self):
        form = PdxForm()
        self.assertEqual(form.fields['passage_number'].help_text, PASSAGES_HELP_TEXT)

    def test_publications_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['publications'].label is None
                        or form.fields['publications'].label == 'Publications')

    def test_validation_techniques_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['validation_techniques'].label is None
                        or form.fields['validation_techniques'].label == 'Validation techniques')

    def test_validation_techniques_help_text(self):
        form = PdxForm()
        self.assertEqual(form.fields['validation_techniques'].help_text, VALIDATION_TECHNIQUES_HELP_TEXT)

    def test_validation_description_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['validation_description'].label is None
                        or form.fields['validation_description'].label == 'Validation description')

    def test_passages_validated_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['passages_validated'].label is None
                        or form.fields['passages_validated'].label == 'Passages validated')

    def test_passages_validated_help_text(self):
        form = PdxForm()
        self.assertEqual(form.fields['passages_validated'].help_text, PASSAGES_HELP_TEXT)

    def test_validation_host_strain_full_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['validation_host_strain_full'].label is None
                        or form.fields['validation_host_strain_full'].label ==
                        'Validation host strain full')

    def test_validation_host_strain_full_help_text(self):
        form = PdxForm()
        self.assertEqual(form.fields['validation_host_strain_full'].help_text, STRAIN_LOOKUP)

    def test_provider_type_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['provider_type'].label is None
                        or form.fields['provider_type'].label == 'Provider type')

    def test_model_accessibility_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['model_accessibility'].label is None
                        or form.fields['model_accessibility'].label == 'Model accessibility')

    def test_europdx_access_modality_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['europdx_access_modality'].label is None
                        or form.fields['europdx_access_modality'].label == 'Europdx access modality')

    def test_contact_email_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['contact_email'].label is None
                        or form.fields['contact_email'].label == 'Contact email')

    def test_contact_name_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['contact_name'].label is None
                        or form.fields['contact_name'].label == 'Contact name')

    def test_provider_name_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['provider_name'].label is None
                        or form.fields['provider_name'].label == 'Provider name')

    def test_provider_abbreviation_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['provider_abbreviation'].label is None
                        or form.fields['provider_abbreviation'].label == 'Provider abbreviation')

    def test_project_name_field_label(self):
        form = PdxForm()
        self.assertTrue(form.fields['project_name'].label is None
                        or form.fields['project_name'].label == 'Project name')
