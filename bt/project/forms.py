from django import forms
from django.db import transaction
from .models import Project,ProjectTeam
from user.models import User

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Project Description'}),
            'technology': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Technology'}),
            'estimatedHours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '12'}),
            'startDate': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'MM/DD/YYYY'}),
            'completionDate': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'MM/DD/YYYY'})
        }

    @transaction.atomic
    def save(self):
        project = super().save(commit=False)
        project.save()
        return project

class ProjectTeamCreationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_developer=True))

    class Meta:
        model = ProjectTeam
        fields = '__all__'
        
        # widgets = {
        #     'project': forms.ChoiceField(attrs={'class': 'form-control'}),
        #     'user': forms.SelectMultiple(attrs={'class': 'form-control'})
        # }

    @transaction.atomic
    def save(self):
        projectteam = super().save(commit=False)
        projectteam.save()
        return projectteam
        