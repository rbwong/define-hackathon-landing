from django import forms
from .models import Team


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ["team_name", "m1_full_name", "m1_school", "m1_course", "m1_contact_num", "m1_email",
                  "m2_full_name", "m2_school", "m2_course", "m2_contact_num", "m2_email",
                  "m3_full_name", "m3_school", "m3_course", "m3_contact_num", "m3_email",
                  "m4_full_name", "m4_school", "m4_course", "m4_contact_num", "m4_email",
                  "m5_full_name", "m5_school", "m5_course", "m5_contact_num", "m5_email", ]

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        provider = contact_number[:4]
        # hardcode at its finest
        if not (provider == "0817" or provider == "0817" or provider == "0905"
                or provider == "0906" or provider == "0907" or provider == "0908" or provider == "0909"
                or provider == "0912" or provider == "0915" or provider == "0916" or provider == "0917" or
                provider == "0918" or provider == "0919" or provider == "0910" or provider == "0921" or provider == "0923" or
                provider == "0925" or provider == "0926" or provider == "0927" or provider == "0928" or provider == "0929" or
                provider == "0932" or provider == "0933" or provider == "0934" or provider == "0935" or provider == "0936" or
                provider == "0937" or provider == "0938" or provider == "0939" or provider == "0942" or provider == "0943" or
                provider == "0946" or provider == "0947" or provider == "0948" or provider == "0949" or provider == "0950" or
                provider == "0973" or provider == "0974" or provider == "0975" or provider == "0977" or provider == "0978" or
                provider == "0979" or provider == "0989" or provider == "0994" or provider == "0996" or provider == "0997" or
                provider == "0998" or provider == "0999"):
            raise forms.ValidationError("Please provide a valid number")
        return contact_number
