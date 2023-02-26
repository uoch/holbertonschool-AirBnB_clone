import unittest
from models.amenity import Amenity


class TestAmanity(unittest.TestCase):

    def test_amenty(self):
        my_user2 = Amenity()
        my_user2.name = "mayouka_evnets"
        my_user2.save()
        self.assertEqual(str(my_user2), str(my_user2))

    def test_all(self):
        self.assertEqual(Amenity.name, "")
