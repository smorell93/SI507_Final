###Install Packages
import os
import pandas as pd
import random
import numpy as np
from flask import Flask, render_template, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

###Initialize Database###
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'kaldsjflsdkf'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./ads_database.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session

#Creating Ad Data
ad_data = pd.read_csv("wmphouse2016.csv")
vidfile_name = ad_data['vidfile']

#Creating Classes
class Advertisement(db.Model):
    __tablename__ = 'Advertisement'
    id = db.Column(db.Integer, primary_key=True)
    NewData = db.relationship("NewInfo", back_populates = "Ad")
    FirstName = db.Column(db.String(250))
    LastName = db.Column(db.String(250))
    State = db.Column(db.String(250))
    District = db.Column(db.String(250))
    Opponent = db.Column(db.String(250))
    VideoFile = db.Column(db.String(250))

    def __repr__(self):
        return "{} {}, a 2016 candidate for the U.S. House of Representatives, is running in {} {} against {}.".format(self.FirstName,self.LastName,self.State,self.District, self.Opponent)

association_table = db.Table('Association', db.Model.metadata, db.Column('NewInfo_id', db.Integer, db.ForeignKey('NewInfo.id')), db.Column('UserInfo_id', db.Integer, db.ForeignKey('UserInfo.id')))

class NewInfo(db.Model):
    __tablename__ = 'NewInfo'
    id = db.Column(db.Integer, primary_key = True)
    Ad_id = db.Column(db.Integer, db.ForeignKey('Advertisement.id'))
    Ad = db.relationship("Advertisement", back_populates="NewData")
    Users = db.relationship("UserInfo", secondary = association_table,backref="Infos")
    Gender = db.Column(db.String(250))
    Transcript = db.Column(db.String(25000))

    def __repr__(self):
        return "{} {} is a {} candidate".format(self.Ad.FirstName, self.Ad.LastName, self.Gender)

class UserInfo(db.Model):
    __tablename__ = 'UserInfo'
    id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(250))
    HoursWorked = db.Column(db.Integer, default = 0)
    AdsCoded = db.Column(db.Integer, default = 0)
    Money = db.Column(db.Integer)

    def __repr__(self):
        return "{} has worked {} hours and coded {} ads.".format(self.Name, self.HoursWorked, self.AdsCoded)

def random_ad(ad_data):
    rand_int = random.randint(1, len(ad_data))
    cand_name = str(ad_data['cand_id'][rand_int])
    new = cand_name.split(", ")
    first_name = new[1]
    last_name = new[0]
    cand_state = ad_data['state'][rand_int]
    cand_district = ad_data['district'][rand_int]
    cand_opponent = str(ad_data['tgt_id'][rand_int])
    if "," in cand_opponent:
        oppnew = cand_opponent.split(", ")
        cand_opponent = str(oppnew[1]) + " " + str(oppnew[0])
    else:
        cand_opponent = str(ad_data['tgt_id'][rand_int])
    ad_title = "VideoFiles/" + str(ad_data['vidfile'][rand_int]) + ".mp4"
#    Candidate = Advertisement.query.filter_by(FirstName = first_name).first()
#    if Candidate:
#        return Candidate
#    else:
    Candidate = Advertisement(FirstName = first_name, LastName = last_name, State = cand_state, District = cand_district, Opponent = cand_opponent, VideoFile = ad_title)
    return Candidate

def calculate_money(User):
    money = int(User.HoursWorked) * 10
    return money

def get_user(user_name):
    user = UserInfo.query.filter_by(Name = user_name).first()
    if user:
        return user
    else:
        user = UserInfo(Name = user_name)
        session.add(user)
        session.commit()
        return user

#Flask Routes
@app.route('/', methods = ['POST', 'GET'])
def greet_user():
    if request.method == "POST":
        return render_template("greetuser.html")
    else:
        return render_template("greetuser.html")

@app.route('/campaign_ad/input', methods = ['POST', 'GET'])
def ad_input():
    ad = random_ad(ad_data)
    session.add(ad)
    session.commit()
    if request.method == "POST":
        ad = random_ad(ad_data)
        session.add(ad)
        session.commit()
        return render_template("userinput.html", first_name = ad.FirstName, last_name = ad.LastName, state = ad.State, district = ad.District, cand_opponent = ad.Opponent, video = ad.VideoFile, id=ad.id)
    else:
        ad = random_ad(ad_data)
        session.add(ad)
        session.commit()
        return render_template("userinput.html", first_name = ad.FirstName, last_name = ad.LastName, state = ad.State, district = ad.District, cand_opponent = ad.Opponent, video = ad.VideoFile, id=ad.id)

@app.route('/campaign_ad/submit/<id>', methods = ['POST', 'GET'])
def ad_submission(id):
    Name = request.form['Name']
    User = UserInfo(Name = Name)
    Gender = request.form['Gender']
    Transcript = request.form['Transcript']
    current_user = get_user(Name)
    if request.method == 'POST':
        Submission = NewInfo(Gender = Gender, Transcript = Transcript, Ad_id = id)
        Submission.Users.append(current_user)
        session.add(Submission)
        session.commit()
        return render_template("submission.html", gender = Submission.Gender, transcript = Submission.Transcript, name = current_user.Name)

@app.route('/user_info/input', methods = ['POST','GET'])
def user_info():
    if request.method == 'POST':
        return render_template("hoursworked.html")
    else:
        return render_template("hoursworked.html")

@app.route('/user_info/submit', methods = ['POST', 'GET'])
def user_submission():
    Name = request.form['Name']
    Hours = int(request.form['Hours'])
    Ads = int(request.form['Ads'])
    current_user2 = get_user(Name)
    if request.method == 'POST':
        current_user2.HoursWorked += Hours
        current_user2.AdsCoded += Ads
        Money = calculate_money(current_user2)
        current_user2.Money = Money
        session.commit()
        return render_template("userhours.html", Name = current_user2.Name, Hours = current_user2.HoursWorked, Ads = current_user2.AdsCoded, Money = current_user2.Money)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
