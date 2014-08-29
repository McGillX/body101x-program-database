from django import forms
from models import Program

EVALUATION = (
	("Any", "Any"),
	('Effective', 'Effective'),
	('Not Effective', 'Not Effective'),
	('Not Studied', 'Not Studied'),
)

TARGET_AUDIENCE = (
	("Any", "Any"),
	("Small Groups (< 20 people)", "Small Groups (< 20 people)"),
	("Large Groups (> 20 people)", "Large Groups (> 20 people)"),
	("Community", "Community"),
	("City", "City"),
	("Country", "Country")
	)

TYPE_OF_EXERCISE = (
	("Any Activity" , "Any Activity"),
	("Walking" , "Walking"),
	("Running" , "Running"),
	("Swimming", "Swimming"),
	("Cycling", "Cycling"),
	("Dance", "Dance"),
	("Yoga", "Yoga"),
	("Tai Chi", "Tai Chi"),
	("Other", "Other"),
	)

# FilterForm to filters programs on the main page
class FilterForm(forms.Form):
	evaluation = forms.ChoiceField(choices=EVALUATION, initial='Any')
	target_audience = forms.ChoiceField(choices=TARGET_AUDIENCE, initial='Any')
	type_of_exercise = forms.ChoiceField(choices=TYPE_OF_EXERCISE, initial='Any Activity')


# ProgramForm to add programs to the table of programs
class ProgramForm(forms.ModelForm):
	class Meta:
		model = Program
		fields = '__all__'