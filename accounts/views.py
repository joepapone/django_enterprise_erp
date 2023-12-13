from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import LoginForm


def logout_user(request):
    logout(request)
    return redirect('/')

# Create your views here.
def login_user(request):
    # Set html page heading
    heading='Login'

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            # Validate user
            if user is not None:
                login(request, user)

                messages.success(request, 'Login sucessful')

                # Redirect to a sucess page
                return redirect('/home')

            else:
                #Return an 'invalid login' error message.
                messages.error(request, 'Invalid username or password!')

            # Redirect to a sucess page
            return redirect('/accounts/login')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {'header':'HEADER', 'heading': heading, 'form': form})




'''
# Login form
@admin.route('/login', methods=('GET', 'POST'))
def login():
    # Set html page heading
    heading='Login'

    # Create form instance
    form = LoginForm()

    # Validate form input
    if form.validate_on_submit():
        # Create model instance with query data
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalars().first()

        print(f'Login user: {user} history requeired')

        # Validate password
        if user.is_valid_password(form.password.data):
            # Add user to session with Flask-Login
            login_user(user, remember=form.remember.data)

            # Inform Flask-Principal the identity changed
            identity_changed.send(current_app._get_current_object(), identity=Identity(user.user_id))

            #return redirect(request.args.get('next') or '/')
            return redirect(request.args.get("next") or url_for("root.home"))

        flash('Error - Invalid user or password!')

        #return redirect(request.args.get("next") or url_for("main.home"))
    return render_template('admin/login.html', header=HEADER, heading=heading, form=form)

    '''