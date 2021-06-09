from django.forms import ModelForm
from .models import Lead

class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'

#s LeadForm(forms.Form):
#first_name = forms.CharField#(max_length=50)
#last_name = forms.CharField#(max_length=50)
#age = forms.IntegerField#(min_value=0)

        