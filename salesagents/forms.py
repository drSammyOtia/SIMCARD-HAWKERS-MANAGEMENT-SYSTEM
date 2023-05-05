from django import forms
from .models import salesAgent


class salesAgentForm(forms.ModelForm):
    class Meta:
        model = salesAgent
        fields = ['agent_serialNo', 'first_name',
                  'surname', 'phone_number', 'assigned_area', 'team_leader', 'status']
        labels = {
            'agent_serialNo': 'Agent SerialNo',
            'first_name': 'First Name',
            'surname': 'Surname',
            'phone_number': 'Phone Number',
            'assigned_area': 'Assigned Area',
            'team_leader': 'Team Leader',
            'status': 'Status'
        }
        widgets = {
            'agent_serialNo': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'assigned_area': forms.TextInput(attrs={'class': 'form-control'}),
            'team_leader': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.BooleanField()
        }
