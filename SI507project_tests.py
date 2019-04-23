from SI507project_tools import *
import unittest

class Tests(unittest.TestCase):

    def test_database_relationship(self):
        TEST = Advertisement(FirstName = "Sara", LastName = "Morell", State = "NY", District = "12", Opponent = "Sara's Evil Twin", VideoFile = "CAMPAIGNAD")
        TEST2 = NewInfo(Ad = TEST, Gender = "Female", Transcript = "Ad Transcript Would Go Here")
        self.assertEqual(TEST2.Ad.FirstName, TEST.FirstName, "Testing that the database relationship back populates")

    def test_randomnumber_Candidate(self):
        ad_data = pd.read_csv("wmphouse2016.csv")
        TEST3 = random_ad(ad_data)
        FN = TEST3.FirstName
        self.assertTrue(FN == "Steve" or FN == "Bradley" or FN == "French" or FN == "Matt" or FN == "Martha" or FN == "Christine", "Testing that the random ad functions pulls from the ad data correctly.")

    def test_CandidateGender(self):
        ad_data = pd.read_csv("wmphouse2016.csv")
        TEST4 = random_ad(ad_data)
        self.assertTrue(isinstance(TEST4.VideoFile,str) == True, "Testing if video file name is a string")

if __name__ == '__main__':
    unittest.main(verbosity=2)


# TEST = Advertisement(FirstName = "Sara", LastName = "Morell", State = "NY", District = "12", Opponent = "Sara's Evil Twin", VideoFile = "CAMPAIGNAD")
# db.create_all()
# session.add(TEST)
# session.commit()
# TEST_A = Advertisement(FirstName = "Bara", LastName = "Borell", State = "BY", District = "B2", Opponent = "Bara's Evil Twin", VideoFile = "BCAMPAIGNAD")
# session.add(TEST_A)
# session.commit()
# TESTB = NewInfo(Ad = TEST_A, Gender = "Male", Transcript = "BAd Transcript Would Go Here")
# session.add(TESTB)
# session.commit()
# TEST2 = NewInfo(Ad = TEST, Gender = "Female", Transcript = "Ad Transcript Would Go Here")
# session.add(TEST2)
# session.commit()
# TEST3 = UserInfo(Name = "Sara", HoursWorked = 5, AdsCoded = 60)
# TEST3.Info = TEST2
# TEST3.Info = TESTB
# session.add(TEST3)
# session.commit()
# print(TEST)
# print(TEST2)
# print(TEST3)
