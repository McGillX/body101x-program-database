from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import FilterForm, ProgramForm
from models import Program

# Create your views here.

# View for main page which will show table of programs and allow user to filter
# programs based on type of exercise, target audience and evaluation
def index(request):
	context = {}
	output = Program.objects.all()
	if request.method == 'POST':
		form = FilterForm(request.POST)
		if form.is_valid():
			form_output = {"evaluation" : request.POST['evaluation'], "target_audience" : request.POST['target_audience'], "type_of_exercise" : request.POST['type_of_exercise']}	
			evaluation, target_audience, type_of_exercise = request.POST['evaluation'], request.POST['target_audience'], request.POST['type_of_exercise']
			if type_of_exercise == "Any Activity" and target_audience == "Any" and evaluation == "Any":
				context = { 'output' : output, 'form' : form, 'form_output' : form_output }
			else:
				result = []
				for item in output:
					# if (evaluation == item["evaluation"] or evaluation == 'Any') and (target_audience == item['target'] or target_audience == 'Any') and (type_of_exercise in item['type'] or type_of_exercise == 'Any Activity'):
					if (evaluation == item.evaluation or evaluation == 'Any') and (target_audience == item.target_audience or target_audience == 'Any') and (type_of_exercise in item.type_of_exercise or type_of_exercise == 'Any Activity'):
						result.append(item)
				if result:
					context = { 'output' : result, 'form' : form, 'form_output' : form_output }
				else:
					context = { 'output' : output, 'form' : form, 'form_output' : form_output }
	else:
		form = FilterForm()
		context = { 'output' : output, 'form' : form }
	return render(request, 'programs/index.html', context)
    #return HttpResponse("Hello, world. You're at the poll index.")

# View to allow adding a program to the table
def add_program(request):
	if request.method == "POST":
		form = ProgramForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = ProgramForm(initial = {"evaluation": "Any", "type_of_exercise" : "Any Activity", "target_audience" : "Any"})


	return render(request, "programs/form.html", {'form' : form})