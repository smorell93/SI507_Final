###Install Packages
import os
import pandas as pd
import random
import numpy as np
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

###Initialize Database###
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'kaldsjflsdkf'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./ads_database.db' # TODO: decide what your new database name will be -- that has to go here
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

class NewInfo(db.Model):
    __tablename__ = 'NewInfo'
    id = db.Column(db.Integer, primary_key = True)
    Ad_id = db.Column(db.Integer, db.ForeignKey('Advertisement.id'))
    Ad = db.relationship("Advertisement", back_populates="NewData")
    Gender = db.Column(db.String(250))
    Transcript = db.Column(db.String(25000))

    def __repr__(self):
        return "{} {} is a {} candidate".format(self.Ad.FirstName, self.Ad.LastName, self.Gender)
#

#
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
    Candidate = Advertisement(FirstName = first_name, LastName = last_name, State = cand_state, District = cand_district, Opponent = cand_opponent, VideoFile = ad_title)
    return Candidate

#Flask Routes
@app.route('/campaign_ad/input')
def video_feed():
    ad = random_ad(ad_data)
    session.add(ad)
    session.commit()
    return render_template("userinput.html", first_name = ad.FirstName, last_name = ad.LastName, state = ad.State, district = ad.District, cand_opponent = ad.Opponent, video = ad.VideoFile)
#
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
