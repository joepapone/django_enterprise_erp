from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods


from hr.models import Department
from hr.forms import DepartmentForm


# Create your views here.
def deparment_list(request):
    department = Department.objects.all()
    return render(request, "department_list.html", {"department_list": department})

def department_add(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = DepartmentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            department = Department(department_name=form.department_name)
            department.save()

            messages.success(request, 'The department has been created successfully.')

            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DepartmentForm()

    return render(request, "department_form.html", {"form": form})

'''
@require_http_methods(["POST"])
def department_add(request):
    name = request.POST["name"]
    department = Department(name=name)
    department.save()
    return redirect("deparment_list")

def department_update(request, department_id):
    department = Department.objects.get(id=department_id)
    department.name = request.POST["name"]
    department.save()
    return redirect("deparment_list")
'''

def department_delete(request, department_id):
    department = Department.objects.get(id=department_id)
    department.delete()
    return redirect("deparment_list")
