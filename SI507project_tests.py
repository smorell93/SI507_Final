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
