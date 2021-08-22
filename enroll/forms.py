from django import forms
from .models import Employee


GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]
class Registration(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model=Employee
        fields=['serial_no','date','employee_name','father_name','gender','residence','dob','physical_fitness','descriptive_marks','refusel_of_certificate','certificate_being_revoked','age','telephone','email','factory','department','examination_after_a_period']
        labels={'serial_no':'Serial Number','date':'Date','employee_name':'Name','father_name':"Father's Name",'gender':'Sex','residence':'Residence','dob':'Date of Birth','physical_fitness':'Physical Fitness','descriptive_marks':'Descriptive Marks','refusel_of_certificate':'Refusel of Certificate','certificate_being_revoked':'Cerificate Being Revoked','age':'Age','telephone':'Mobile No.','email':'Email','factory':'Name of the factory in which employed','department':'Department in which Employed','examination_after_a_period':'Examination after a Period'}
        widgets={
            'serial_no':forms.NumberInput(attrs={'class':'form-control','id':'serial_noid'}),
            'date':forms.DateInput(attrs={'class':'form-control'}),
            'employee_name':forms.TextInput(attrs={'class':'form-control','id':'employee_nameid'}),
            'father_name':forms.TextInput(attrs={'class':'form-control'}),
            'residence':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'physical_fitness':forms.TextInput(attrs={'class':'form-control'}),
            'descriptive_marks':forms.TextInput(attrs={'class':'form-control'}),
            'refusel_of_certificate':forms.TextInput(attrs={'class':'form-control'}),
            'certificate_being_revoked':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'telephone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'factory':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'examination_after_a_period':forms.TextInput(attrs={'class':'form-control'})

        }
        