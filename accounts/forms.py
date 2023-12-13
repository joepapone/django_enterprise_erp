from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", min_length=5, max_length=32, widget=forms.PasswordInput)

'''
# Login from attributes
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[InputRequired(), Email()], description="User email",
        render_kw={'class': 'field-data', 'placeholder': 'Email..', 'autofocus': ""})
    password = PasswordField(label='Password', validators=[InputRequired()], description="User password",
        render_kw={'class': 'field-data', 'placeholder': 'Password..'})
    remember = BooleanField(label='Remember Me', description="Remember me",
        render_kw={'class': 'field-label', 'type': 'checkbox'})

    # Validator will run after all validators have passed
    def validate_password(form, field):
        try:
            user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalars().one()
        except (MultipleResultsFound, NoResultFound):
            raise ValidationError("Invalid user")
        if user is None:
            raise ValidationError("Invalid user")
        if not user.is_valid_password(form.password.data):
            raise ValidationError("Invalid password")

        # Assign user
        form.user = user
'''