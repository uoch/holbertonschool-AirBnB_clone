
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_place(self):
        my_user2 = Place()
        my_user2.city_id = "ariana"
        my_user2.user_id = "mayouka"
        my_user2.name = "John"
        my_user2.save()
        self.assertEqual(str(my_user2), str(my_user2))

    def test_all(self):
        self.assertEqual(Place.city_id, "")
