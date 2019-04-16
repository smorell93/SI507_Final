from SI507_finalproject import *
import unittest

class StepOne(unittest.TestCase):

    def test_database_relationship(self):
        TEST = Advertisement(FirstName = "Sara", LastName = "Morell", State = "NY", District = "12", Opponent = "Sara's Evil Twin", VideoFile = "CAMPAIGNAD")
        TEST2 = NewInfo(Ad = TEST, Gender = "Female", Transcript = "Ad Transcript Would Go Here")
        self.assertEqual(TEST2.Ad.FirstName, TEST.FirstName, "Testing that the database relationship back populates")

    def test_randomnumber(self):
        ad_data = pd.read_csv("wmphouse2016.csv")
        TEST3 = random_ad(ad_data)
        FN = TEST3.FirstName
        self.assertTrue(FN == "Steve" or FN == "Bradley" or FN == "French" or FN == "Matt" or FN == "Martha" or FN == "Christine", "Testing that the random ad functions pulls from the ad data correctly.")

    def test_user_inputs(self):
        pass
        #Once I determine the values that the user inputs will be saved as, I will test them here


if __name__ == '__main__':
    unittest.main(verbosity=2)
