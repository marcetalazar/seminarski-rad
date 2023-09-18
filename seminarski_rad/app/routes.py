from app import app,db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm,RegistrationForm, EditProfileForm
from app.models import User
from flask_login import login_user,current_user,logout_user
from werkzeug.urls import url_parse




@app.route('/',methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template('index.html',title='Pyflora')



@app.route('/sign_in',methods=['GET','POST'])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('about_app'))
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
    
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            
            return redirect(url_for('sign_in'))
        login_user(user,remember=True)
        next_page = request.args.get('next')    
        
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('about_app')
        return redirect(next_page)
    return render_template('sign_in.html', title='Sign In', form=form)

@app.route('/register',methods=['GET','POST'])
def register_user():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(name=form.name.data.capitalize(),last_name=form.last_name.data.capitalize(),username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are successfully registered,you can login now')
        return redirect(url_for('sign_in'))
   

    return render_template('register_user.html', title='Register', form=form)


@app.route('/about_app',methods=['GET','POST'])
def about_app():
    return render_template('about_app.html',title='about App')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile',methods=['GET','POST'])
def profile():
     return render_template('profile.html',title='Your profile')
 

@app.route('/edit_profile',methods=['GET','POST'])
def edit_profile():
    form=EditProfileForm()
    if form.validate_on_submit():
        pass
    return render_template('edit_profile.html',title='Edit profile') 