from SI507_finalproject import *
import unittest

class StepOne(unittest.TestCase):
    def test_video_file(self):
        pass
        #This will test whether the file printing to Canvas ends in "wmv"
        #This will also test whether the video file starts with House

    def test_flask_video(self):
        pass
        #This will test whether it is possible to play the video in the flask app

    def test_candidate_info(self):
        pass
        #This will test whether the type of the candidate info is a string
        #This will also test whether the first letter is capital and the second letter is lowercase

    def test_user_inputs(self):
        pass
        #This

TEST = Advertisement(FirstName = "Sara", LastName = "Morell", State = "NY", District = "12", Opponent = "Nick Paulson", VideoFile = "CAMPAIGNAD")
db.create_all()
session.add(TEST)
session.commit()
TEST2 = NewInfo(Ad = TEST, Gender = "Female", Transcript = "Ad Transcript Would Go Here")
session.add(TEST2)
session.commit()
print(TEST2)
