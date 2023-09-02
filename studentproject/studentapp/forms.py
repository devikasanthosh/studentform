from django.forms import forms
from .models import Student
from .models import *	
from django import forms
from .models import Student		
 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"