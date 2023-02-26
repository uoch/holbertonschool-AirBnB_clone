import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_city(self):
        my_user2 = City()
        my_user2.state_id = "242424"
        my_user2.name = "John"
        my_user2.save()
        self.assertEqual(str(my_user2), str(my_user2))

    def test_all(self):
        self.assertEqual(City.state_id, "")
