from flask_wtf import FlaskForm
from wtforms import Form, FieldList, FormField, IntegerField, SelectField, \
        StringField, TextAreaField, SubmitField,SelectMultipleField
from wtforms import validators

class VulnerabilitySubPartsForm(Form):
    """Subform.

    CSRF is disabled for this subform (using `Form` as parent class) because
    it is never used by itself.
    """
    part_label = StringField(
        'Label',
        validators=[validators.InputRequired(), validators.Length(max=100)]
    )
    
    protection_factor = StringField(
        'Protection Factor',
        validators=[validators.Length(max=255)]
    )

    key = StringField(
        'Key',
        validators=[validators.Length(max=255)]
    )

    ca = StringField(
        'CA',
        validators=[validators.Length(max=255)]
    )


class VulnerabilityPartsForm(Form):
    """Subform.

    CSRF is disabled for this subform (using `Form` as parent class) because
    it is never used by itself.
    """
    part_label = StringField(
        'Label',
        validators=[validators.InputRequired(), validators.Length(max=100)]
    )

    sub_parts = FieldList(
        FormField(VulnerabilitySubPartsForm),
        min_entries=1,
        max_entries=20
    )


class ControlForm(FlaskForm):
    """Parent form."""

    id = IntegerField(
        'ID',
        validators=[validators.InputRequired()]
    )

    family = SelectField(
        'Family',
        validators=[validators.InputRequired()],
        choices=[
            ('AC', 'Access Control'), 
            ('MP', 'Media Protection'), 
            ('PE', 'Physical and Environmental Protection'),
            ('PL', 'Planning'),
            ('PM', 'Program Management'),
            ('PS', 'Personnel Security'),
            ('RA', 'Risk Assessment'),
            ('SA', 'System and Services Acquisition'),
            ('SC', 'System and Communications Protection'),
            ('SI', 'System and Information Integrity'),
            ('AT', 'Awareness and Training'),
        ]
    )

    control_label = StringField(
        'Control Label',
        validators=[validators.InputRequired()]
    )

    vulnerability_label = StringField(
        'Vulnerability Label',
        validators=[validators.InputRequired()]
    ) 

    vulnerability_level = StringField(
        'Vulnerability Level',
        validators=[validators.InputRequired()]
    )   

    threats = SelectMultipleField(
        'Threats',
        validators=[validators.InputRequired()],
        choices=[
            ('THR_IAOC', 'Intentional acts of conflict'), 
            ('THR_IMAR', 'Intentional misappropriation of resources'), 
            ('THR_IMUR', 'Intentional misuse of resources'),
            ('THR_UMUR', 'Unintentional technology failure'),
            ('THR_UNC', 'Unintentional misuse of resources'),
            ('THR_NDIS', 'Unintentional non-compliance'),
            ('THR_HDIS', 'Natural disasters'),
        ]
    )  
 
    control_parts = TextAreaField(
        'Control Parts',
        validators=[]
    )

    vulnerability_parts = TextAreaField(
        'Vulnerability Parts',
        validators=[]
    )


class SettingsForm(FlaskForm):
    """Parent form."""

    id = StringField(
        'ID',
        validators=[validators.InputRequired()]
    )

    settings_label = StringField(
        'Label',
        validators=[validators.InputRequired()]
    )

    level = SelectField(
        'level',
        validators=[validators.InputRequired()],
        choices=[
            ('tenant', 'Tenant'), 
            ('project', 'Project'), 
            ('admin', 'Admin'),
            ('fcr', 'FCR'),
        ]
    )
   
    parts = TextAreaField(
        'Parts',
        validators=[]
    )

class ThreatForm(FlaskForm):
    """Parent form."""

    id = StringField(
        'ID',
        validators=[validators.InputRequired()]
    )

    threat_label = StringField(
        'Label',
        validators=[validators.InputRequired()]
    )

    level = SelectField(
        'level',
        validators=[validators.InputRequired()],
        choices=[
            ('tenant', 'Tenant'), 
            ('project', 'Project'), 
            ('admin', 'Admin'),
            ('fcr', 'FCR'),
        ]
    )
   
    parts = TextAreaField(
        'Parts',
        validators=[]
    )