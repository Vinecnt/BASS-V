from django import forms
from .models import *

class AddNewAssignmentForm(forms.ModelForm):
    #
    # # name of new assignment
    # a_name = forms.CharField(help_text="Enter the name of the assignment")
    #
    # # number of assigned hours
    # assigned_hours = forms.CharField(help_text="Enter the assigned hours for this assignment")

    class Meta:
            model = Assignment
            fields = ['aname','assigned_hours']
