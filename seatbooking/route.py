from flask import render_template, url_for, flash, redirect, request
from seatbooking import app, db, bcrypt
from seatbooking.forms import RegistrationForm, LoginForm
from seatbooking.models import User
from flask_login import login_user, current_user, logout_user, login_required
from seatbooking.aibooking import alloc


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('profile'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        alloc_gender = str(form.gender.data).capitalize()
        alloc_ca = str(form.ca.data).capitalize()
        user = str(form.username.data).capitalize()
        alloc_seat,alloc_coach = alloc(form.age.data, form.ca.data)
        if(alloc_seat%3==0):
            alloc_berth = 'Upper'
        elif ((alloc_seat+1)%3==0):
            alloc_berth = 'Middle'
        elif ((alloc_seat+2)%3==0):
            alloc_berth = 'Lower'
        user = User(username=user, email=form.email.data, password=hashed_password, age=form.age.data,  gender=alloc_gender, ca=alloc_ca, seat=alloc_seat, coach=alloc_coach, berth= alloc_berth)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('profile'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')

@app.route('/booking_info')
@login_required
def booking_info():
    return render_template('booking_info.html')

@app.route('/booking_invoice', methods=['GET', 'POST'])
@login_required
def booking_invoice():
    return render_template('booking_invoice.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
