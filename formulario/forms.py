from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from formulario.models import basede2
from django import forms



class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}

class segundo(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = basede2
        fields = ['edad']