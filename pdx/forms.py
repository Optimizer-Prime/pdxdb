from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset, Reset

from .models import Pdx

# patient info
PATIENT_ID_PLACEHOLDER = 'e.g. A08593'
PATIENT_HISTORY_PLACEHOLDER = 'If available, please provide relevant medical history.'
INITIAL_DIAGNOSIS_PLACEHOLDER = 'If available, first diagnosis for this patient.'

# patient tumor at collection time
SAMPLE_ID_PLACEHOLDER = 'e.g. A08593_001'
TUMOR_TYPE_PLACEHOLDER = 'primary, metastatic'
PRIMARY_SITE_PLACEHOLDER = 'e.g. right breast, liver, brain'
COLLECTION_EVENT_PLACEHOLDER = 'e.g. collection 2'
VIROLOGY_STATUS_PLACEHOLDER = 'e.g. human papillomavirus, Epstein-Barr virus'

# pdx model details
MODEL_ID_PLACEHOLDER = 'e.g. ABC_001'
HOST_STRAIN_PLACEHOLDER = 'NOD SCID GAMMA'
HOST_STRAIN_FULL_PLACEHOLDER = 'NOD.Cg-Prkdcscid Il2rgtm1Wjl/SzJ'
ENGRAFTMENT_SITE_PLACEHOLDER = 'e.g. mammary fat pads'
ENGRAFTMENT_TYPE_PLACEHOLDER = 'e.g. orthotopic, heterotopic'
SAMPLE_TYPE_PLACEHOLDER = 'e.g. tissue fragment, dissociated cells'
SAMPLE_STATE_PLACEHOLDER = 'e.g. fresh, frozen'
PUBLICATIONS_PLACEHOLDER = 'Provide comma separated list of any publications model was used in.'

# pdx model validation
VALIDATION_TECHNIQUES_PLACEHOLDER = 'e.g. fingerprinting, histology, immunohistochemistry'
VALIDATION_DESCRIPTION_PLACEHOLDER = 'high, good, moderate concordance'
PASSAGES_PLACEHOLDER = 'e.g. 0, 1, 2'

# sharing and contact
PROVIDER_TYPE_PLACEHOLDER = 'e.g. academia, CRO, pharma'
MODEL_ACCESS_PLACEHOLDER = 'academia, industry, both'
PROVIDER_NAME_PLACEHOLDER = 'university, company'

# other constants
UNIQUE = 'Must be unique.'
STRAIN_LOOKUP = "Look up <a href='http://www.informatics.jax.org/home/strain' " \
                "target='_blank' rel='noopener noreferrer'>here.</a>"


class PdxForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PdxForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset("<a href='#' target='_blank' rel='noopener noreferrer'>Patient Info</a>",
                     Row(
                         Column('patient_id', css_class='form-group col-md-3 mb-0'),
                         Column('patient_sex', css_class='form-group col-md-2 mb-0'),
                         Column('patient_ethnicity', css_class='form-group col-md-2 mb-0'),
                         Column('ethnicity_assessment_method', css_class='form-group col-md-3 mb-0'),
                         Column('age_at_initial_diagnosis', css_class='form-group col-md-2 mb-0'),
                     ),
                     Row(
                         Column('patient_history', css_class='form-group col-md-6 mb-0'),
                         Column('initial_diagnosis', css_class='form-group col-md-6 mb-0'),
                     )
                     ),
            Fieldset("<a href='#' target='_blank' rel='noopener noreferrer'>Patient Tumor at Collection Time</a>",
                     Row(
                         Column('sample_id', css_class='form-group col-md-3 mb-0'),
                         Column('collection_date', css_class='form-group col-md-3 mb-0'),
                         Column('collection_event', css_class='form-group col-md-3 mb-0'),
                         Column('months_since_collection_one', css_class='form-group col-md-3 mb-0'),
                     ),
                     Row(
                         Column('diagnosis', css_class='form-group col-md-6 mb-0'),
                         Column('diagnosis_notes', css_class='form-group col-md-6 mb-0'),
                     ),
                     Row(
                         Column('age_in_years_at_collection', css_class='form-group col-md-3 mb-0'),
                         Column('tumor_type', css_class='form-group col-md-3 mb-0'),
                         Column('primary_site', css_class='form-group col-md-3 mb-0'),
                         Column('collection_site', css_class='form-group col-md-3 mb-0'),
                     ),
                     Row(
                         Column('stage', css_class='form-group col-md-3 mb-0'),
                         Column('staging_system', css_class='form-group col-md-3 mb-0'),
                         Column('grade', css_class='form-group col-md-3 mb-0'),
                         Column('grading_system', css_class='form-group col-md-3 mb-0'),
                     ),
                     Row(
                         Column('treatment_info_shareable', css_class='form-group col-md-3 mb-0'),
                         Column('treatment_naive_at_collection', css_class='form-group col-md-3 mb-0'),
                         Column('treated', css_class='form-group col-md-3 mb-0'),
                         Column('prior_treatment', css_class='form-group col-md-3 mb-0'),
                         Column('virology_status', css_class='form-group col-md-6 mb-0'),
                     )
                     ),
            Fieldset("<a href='#' target='_blank' rel='noopener noreferrer'>PDX Model Details</a>",
                     Row(
                         Column('model_id', css_class='form-group col-md-3 mb-0'),
                         Column('host_strain', css_class='form-group col-md-3 mb-0'),
                         Column('host_strain_full', css_class='form-group col-md-6 mb-0'),
                     ),
                     Row(
                         Column('engraftment_site', css_class='form-group col-md-3 mb-0'),
                         Column('engraftment_type', css_class='form-group col-md-3 mb-0'),
                         Column('sample_type', css_class='form-group col-md-3 mb-0'),
                         Column('sample_state', css_class='form-group col-md-3 mb-0'),
                     ),
                     Row(
                         Column('passage_number', css_class='form-group col-md-3 mb-0'),
                         Column('publications', css_class='form-group col-md-9 mb-0'),
                     )
                     ),
            Fieldset("<a href='#' target='_blank' rel='noopener noreferrer'>PDX Model Validation</a>",
                     Row(
                         Column('validation_techniques', css_class='form-group col-md-6 mb-0'),
                         Column('validation_description', css_class='form-group col-md-6 mb-0'),
                     ),
                     Row(
                         Column('passages_validated', css_class='form-group col-md-3 mb-0'),
                         Column('validation_host_strain_full', css_class='form-group col-md-9 mb-0'),
                     )
                     ),
            Fieldset("<a href='#' target='_blank' rel='noopener noreferrer'>Sharing and Contact</a>",
                     Row(
                         Column('provider_type', css_class='form-group col-md-4 mb-0'),
                         Column('model_accessibility', css_class='form-group col-md-4 mb-0'),
                         Column('europdx_access_modality', css_class='form-group col-md-4 mb-0'),
                     ),
                     Row(
                         Column('contact_email', css_class='form-group col-md-3 mb-0'),
                         Column('contact_name', css_class='form-group col-md-2 mb-0'),
                         Column('provider_name', css_class='form-group col-md-2 mb-0'),
                         Column('provider_abbreviation', css_class='form-group col-md-2 mb-0'),
                         Column('project_name', css_class='form-group col-md-3 mb-0'),
                     )
                     ),
            Submit('submit', 'Submit'),
            Reset('reset', 'Reset', css_class='btn-danger'))

        # patient info section of models.py
        self.fields['patient_id'].widget.attrs['placeholder'] = PATIENT_ID_PLACEHOLDER
        self.fields['patient_history'].widget.attrs['rows'] = 3
        self.fields['patient_history'].widget.attrs['placeholder'] = PATIENT_HISTORY_PLACEHOLDER
        self.fields['initial_diagnosis'].widget.attrs['rows'] = 3
        self.fields['initial_diagnosis'].widget.attrs['placeholder'] = INITIAL_DIAGNOSIS_PLACEHOLDER

        # patient tumor at collection time section of models.py
        self.fields['sample_id'].widget.attrs['placeholder'] = SAMPLE_ID_PLACEHOLDER
        self.fields['collection_date'].widget.attrs['class'] = 'datepicker'
        self.fields['collection_event'].widget.attrs['placeholder'] = COLLECTION_EVENT_PLACEHOLDER
        self.fields['diagnosis'].widget.attrs['rows'] = 3
        self.fields['diagnosis_notes'].widget.attrs['rows'] = 3
        self.fields['tumor_type'].widget.attrs['placeholder'] = TUMOR_TYPE_PLACEHOLDER
        self.fields['primary_site'].widget.attrs['placeholder'] = PRIMARY_SITE_PLACEHOLDER
        self.fields['collection_site'].widget.attrs['placeholder'] = PRIMARY_SITE_PLACEHOLDER
        self.fields['virology_status'].widget.attrs['rows'] = 1
        self.fields['virology_status'].widget.attrs['placeholder'] = VIROLOGY_STATUS_PLACEHOLDER

        # pdx model detail section of models.py
        self.fields['model_id'].widget.attrs['placeholder'] = MODEL_ID_PLACEHOLDER
        self.fields['host_strain'].widget.attrs['placeholder'] = HOST_STRAIN_PLACEHOLDER
        self.fields['host_strain_full'].widget.attrs['rows'] = 1
        self.fields['host_strain_full'].widget.attrs['placeholder'] = HOST_STRAIN_FULL_PLACEHOLDER
        self.fields['engraftment_site'].widget.attrs['placeholder'] = ENGRAFTMENT_SITE_PLACEHOLDER
        self.fields['engraftment_type'].widget.attrs['placeholder'] = ENGRAFTMENT_TYPE_PLACEHOLDER
        self.fields['sample_type'].widget.attrs['placeholder'] = SAMPLE_TYPE_PLACEHOLDER
        self.fields['sample_state'].widget.attrs['placeholder'] = SAMPLE_STATE_PLACEHOLDER
        self.fields['passage_number'].widget.attrs['placeholder'] = PASSAGES_PLACEHOLDER
        self.fields['publications'].widget.attrs['rows'] = 1
        self.fields['publications'].widget.attrs['placeholder'] = PUBLICATIONS_PLACEHOLDER

        # pdx model validation section of models.py
        self.fields['validation_techniques'].widget.attrs['rows'] = 1
        self.fields['validation_techniques'].widget.attrs['placeholder'] = VALIDATION_TECHNIQUES_PLACEHOLDER
        self.fields['validation_description'].widget.attrs['rows'] = 1
        self.fields['validation_description'].widget.attrs['placeholder'] = VALIDATION_DESCRIPTION_PLACEHOLDER
        self.fields['passages_validated'].widget.attrs['placeholder'] = PASSAGES_PLACEHOLDER
        self.fields['validation_host_strain_full'].widget.attrs['rows'] = 1
        self.fields['validation_host_strain_full'].widget.attrs['placeholder'] = HOST_STRAIN_FULL_PLACEHOLDER

        # sharing and contact section of models.py
        self.fields['provider_type'].widget.attrs['placeholder'] = PROVIDER_TYPE_PLACEHOLDER
        self.fields['model_accessibility'].widget.attrs['placeholder'] = MODEL_ACCESS_PLACEHOLDER
        self.fields['provider_name'].widget.attrs['placeholder'] = PROVIDER_NAME_PLACEHOLDER

    class Meta:
        model = Pdx
        fields = ['patient_id', 'patient_sex', 'patient_ethnicity', 'patient_history',
                  'initial_diagnosis', 'ethnicity_assessment_method', 'age_at_initial_diagnosis',
                  'sample_id', 'collection_date', 'collection_event', 'months_since_collection_one',
                  'age_in_years_at_collection', 'diagnosis', 'diagnosis_notes', 'tumor_type',
                  'primary_site', 'collection_site', 'stage', 'staging_system', 'grade',
                  'grading_system', 'virology_status', 'treatment_info_shareable', 'treatment_naive_at_collection',
                  'treated', 'prior_treatment', 'model_id', 'host_strain', 'host_strain_full',
                  'engraftment_site', 'engraftment_type', 'sample_type', 'sample_state', 'passage_number',
                  'publications', 'validation_techniques', 'validation_description', 'passages_validated',
                  'validation_host_strain_full', 'provider_type', 'model_accessibility',
                  'europdx_access_modality', 'contact_email', 'contact_name', 'provider_name',
                  'provider_abbreviation', 'project_name', ]
        help_texts = {'sample_id': UNIQUE, 'model_id': UNIQUE,
                      'validation_techniques': 'List all that apply. Separate with comma.',
                      'validation_description': 'Must be clear if model is validated or not.',
                      'passage_number': 'Comma seperated list of passage numbers.',
                      'collection_event': 'If collection date entered, leave blank.',
                      'virology_status': 'List all viruses the patient tested positive for. Provide full name. '
                                         'Separate with comma.',
                      'host_strain_full': STRAIN_LOOKUP, 'validation_host_strain_full': STRAIN_LOOKUP,
                      }
