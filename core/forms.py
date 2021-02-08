from django import forms
from .models import Data

class DataModelForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']

    def clean_budget(self):
        budget = self.cleaned_data['budget']
        if float(budget):
            return budget
        elif float(budget.replace('€','')):
            print('--------- inter')
            return budget.replace('€','')
        print('------- out')
