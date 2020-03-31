#importing modules for getting the best site
import json
import math as Math

#importing libraries for Authentication System
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

filename = "VacantLand_Dallas"  # File for Property for Sale Coordinates
filename2 = "DallasHospitals"  # File for Hospital Coordinates

with open(filename + '.json', 'r') as file:  # Loading json data of Property for Sale
    properties_json = json.load(file)
with open(filename2 + '.json', 'r') as file2:  # Loading json data of Hospital
    properties_json2 = json.load(file2)

lat1 = list()
lon1 = list()
lat2 = list()
lon2 = list()
add = list()
img = list()

# Assigning variables, the keys for latitude and longitude in json file
lat = 'latitude'
lon = 'longitude'
prop_address = 'address'
title = 'title'
i = 0

# Storing json data of Lat and Long. of each file in a separate list respectively

for properties in properties_json:
    lat1.append(properties[lat])
    lon1.append(properties[lon])
    add.append(properties[prop_address][title])
    img.append(properties['imageUrl'])
    i = i + 1
print("----------------------------------------------------------------------------------------------------------")
i = 0
for properties in properties_json2:
    lat2.append(properties[lat])
    lon2.append(properties[lon])
    i = i + 1


# Calculating distance between land on sale and nearby hospital using standard formulae based on Latitude and Longitude
def degreesToRadians(degrees):
    return degrees * Math.pi / 180


def distanceInKmBetweenEarthCoordinates(lat1, lon1, lat2, lon2):
    earthRadiuskm = 6371

    dLat = degreesToRadians(lat2 - lat1)
    dLon = degreesToRadians(lon2 - lon1)

    lat1 = degreesToRadians(lat1)
    lat2 = degreesToRadians(lat2)

    a = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.sin(dLon / 2) * Math.sin(dLon / 2) * Math.cos(lat1) * Math.cos(
        lat2)
    c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
    return (earthRadiuskm * c)

distance = list()
latitude = list()
longitude = list()
num_Hosp = list()
address = list()
imageurl = list()

# def in_range_check(latt, lont, lath, lonh, count, j):
#     #for j in range(0,len(lon1)):
#     dis = distanceInKmBetweenEarthCoordinates(latt, lont, lath, lonh) #
#     if(dis<=3 or j <= len(lath)-1):
#         count = count+1  #Counting number of such hospitals
#         in_range_check(latt, lont, lath, lonh, count, j+1)
#     else:
#         return count
# j=0
for i in range(0, len(lat1)):
    count = 0
    for j in range(len(lat2)):
        dis = distanceInKmBetweenEarthCoordinates(lat1[i], lon1[i], lat2[j], lon2[j])

        # Selecting the Property having a hospital in the range of 3Km
        if (dis <= 1):
            count = count + 1  # Counting number of such hospitals

    if count > 0:  # Check for whether the given property has at least one hospital in the given range
        latitude.append(lat1[i])
        longitude.append(lon1[i])
        address.append(add[i])
        imageurl.append(img[i])
        num_Hosp.append(count)
    distance.clear()

coordinates = list()
for i in range(len(address)):
    coordinates.append({'address': address[i], 'lat': latitude[i], 'lng': longitude[i], 'imageurl' : imageurl[i]})

print("-----------------------------------------------------------------------------------------------------------")

# Authentication Starts
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # noqa
    username = db.Column(db.String(15), unique=True)  # noqa
    email = db.Column(db.String(50), unique=True)  # noqa
    password = db.Column(db.String(80))  # noqa


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


db.create_all()

@app.route('/Redirect')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('services'))

        return '<h1>Invalid username or password</h1>'
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username = form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        #return '<h1>New user has been created!</h1>'
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('Redirect'))

#Authentication Ends

# Routes for webpage
@app.route("/")

def home():
    return render_template('index_main.html')

@app.route("/about")

def about():
    return render_template('about.html')

@app.route('/contact')

def contacts():
    return render_template('contact.html')

# Map integration with the web app
@app.route("/services")
#decorator, just a way to add functionality to ezisting function
def services():
    return render_template('services.html', coords = coordinates)

if __name__ == "__main__":
    app.run(debug=True)