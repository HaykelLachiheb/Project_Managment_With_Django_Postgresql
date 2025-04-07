# utilisateurs/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ConnexionForm(AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)



from django import forms

class SuppressionForm(forms.Form):
    confirmation = forms.BooleanField(required=True, label="Confirmer la suppression")



from django import forms
from .models import Tasks

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['TaskID', 'TaskDaysAllowed', 'TaskDaysWorked','TaskDesc','StartingDay']  # Remplacez par les champs de votre modèle


# forms.py

from django import forms
from .models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['TaskID', 'TaskDaysAllowed','TaskDaysWorked','TaskDesc','StartingDay']



# forms.py
from django import forms

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'class': 'form-control'}))


