from django import forms

from models import Resume
from models import Skill
from models import Experience
from models import Education
from models import Language

from choices import GENDER_CHOICES
from choices import MARITAL_CHOICES
from choices import LANG_LEVEL_CHOICES

class ResumeForm(forms.ModelForm):
    first_name      = forms.CharField(  widget = forms.TextInput(attrs = { 'class': 'radius' }), required = False)
    last_name       = forms.CharField(  widget = forms.TextInput(attrs = { 'class': 'radius' }), required = False)
    date_of_birth   = forms.DateField(  widget = forms.TextInput(attrs = { 'class': 'dp radius' }), input_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], required = False)
    gender          = forms.ChoiceField(widget = forms.Select(attrs={'class':'radius'}), choices = GENDER_CHOICES, required = False)        
    marital_status  = forms.ChoiceField(widget=forms.Select(attrs={'class':'radius'}), choices = MARITAL_CHOICES, required = False)
    summary         = forms.CharField(  widget=forms.Textarea(attrs = { 'class' : 'radius' }), required = False)
    email           = forms.EmailField( required = False)
    address         = forms.CharField(  widget=forms.TextInput(attrs = { 'class': 'radius' }), required = False)
    phone           = forms.CharField(  widget=forms.TextInput(attrs = { 'class': 'radius' }), required = False)
    skype           = forms.CharField(  widget=forms.TextInput(attrs = { 'class': 'radius' }), required = False)
    
    class Meta:
        model   = Resume
        exclude = ('created_at', 'updated_at', 'user')

#  --------------------------------------------------------------------------        

class SkillForm(forms.ModelForm):
    title           = forms.CharField(  widget = forms.TextInput(attrs = { 'class': 'radius' }))
    score           = forms.CharField(  widget = forms.TextInput(attrs = { 'class': 'radius' }), required = False)
    
    class Meta:
        model   = Skill
        exclude = ('created_at', 'updated_at', 'resume')
        
#  --------------------------------------------------------------------------        

class ExpForm(forms.ModelForm):
    title           = forms.CharField(  widget = forms.TextInput(attrs = { 'class': 'radius' }))
    desc            = forms.CharField(  widget= forms.Textarea(attrs = { 'class' : 'radius' }), required = False, label='Description')
    duration        = forms.CharField(  widget = forms.TextInput(attrs = { 'class': 'radius' }), required = False)
    role            = forms.CharField(  widget = forms.TextInput(attrs = { 'class': 'radius' }), required = False)
    
    class Meta:
        model   = Experience
        exclude = ('created_at', 'updated_at', 'resume')
        
#  --------------------------------------------------------------------------        

class EduForm(forms.ModelForm):
    institution     = forms.CharField(  widget = forms.TextInput(attrs = { 'class': 'radius' }))
    specialization  = forms.CharField(  widget = forms.TextInput(attrs = { 'class': 'radius' }))
    graduated_at    = forms.DateField(  widget = forms.TextInput(attrs = { 'class': 'dp radius' }), input_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], required = False)
    
    class Meta:
        model   = Education
        exclude = ('created_at', 'updated_at', 'resume')
        
#  --------------------------------------------------------------------------        

class LangForm(forms.ModelForm):
    name            = forms.CharField(  widget = forms.TextInput(attrs = { 'class': 'radius' }))
    level           = forms.ChoiceField(widget = forms.Select(attrs={'class':'radius'}), choices = LANG_LEVEL_CHOICES, required = False)
    
    class Meta:
        model   = Language
        exclude = ('created_at', 'updated_at', 'resume')