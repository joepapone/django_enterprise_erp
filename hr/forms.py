from django import forms


class DepartmentForm(forms.Form):
    department_name = forms.CharField(label="Department", min_length=3, max_length=50)

'''
class DepartmentForm(FlaskForm):
    department_name = StringField(label='Department', validators=[length(min=3, max=50), department_duplicate], description="Department name",
    render_kw={'class': 'field-data', 'placeholder': 'Name..', 'autofocus': ""})
'''
