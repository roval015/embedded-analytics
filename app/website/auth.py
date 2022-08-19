from unittest import removeResult
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# LOGIN Path
# The user will be asked to enter the email and password
@auth.route('/login', methods=['GET', 'POST'])
def login():
    user_role = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check the database if there if the email already exists.
        user = User.query.filter_by(email=email).first()
        
        if user:
            user_role = user.role
            # Compare the hashed password if they are the same
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                # Redirect to the homepage
                return redirect(url_for('views.home', role=user_role))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    # Render the Login Page
    return render_template('login.html', user=current_user, role=user_role)

# LOGOUT Path
# Once the user logouts, redirect to the login page.
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# SIGN UP Path
# The user will be asked to input the email, fname, lname, pw1, pw2, and role
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    user_role = None
    if request.method == 'POST':
        # Get the details from the request forms
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        role = request.form.get('roles')

        user_role = role

        # Check if the email exists in the database
        user = User.query.filter_by(email=email).first()

        # Output the error detail accordingly
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # If the user does not exist in the database, store the user details. Encrypt the password as well.
            new_user = User(email=email, first_name=first_name, last_name=last_name, role=role, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            # Redirect the user to the Login Page
            return redirect(url_for('auth.login', role=user_role))

    # Render the Sign Up Page
    return render_template('sign_up.html', user=current_user, role=user_role)
