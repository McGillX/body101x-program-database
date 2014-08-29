from django.db import models

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

# Define the database fields for the Program model
class Program(models.Model):
	program = models.CharField(max_length=100)
	type_of_exercise = models.CharField(max_length=100, choices=TYPE_OF_EXERCISE)
	#type_of_exercise = models.ManyToManyField(TypeOfExercise)
	target_audience = models.CharField(max_length=100, choices=TARGET_AUDIENCE)
	description_of_program = models.TextField()
	evaluation = models.CharField(max_length=100, choices=EVALUATION)
	developed_by = models.TextField()
	references = models.TextField()

	def __unicode__(self):
		return self.program + ", " + self.type_of_exercise + ", " + self.target_audience + ", " + self.description_of_program + ", " + self.evaluation + ", " + self.developed_by + ", " + self.references