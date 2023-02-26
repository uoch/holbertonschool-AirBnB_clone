
#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import json

class testBase_AirBnB(unittest.TestCase):

    def test_to_id(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_model_json = "{'my_number': 89, 'name': 'My First Model', 'updated_at': '2023-02-20 14:24:01.871493', 'id': '853d2737-0bc7-4dbe-a403-b3934a3de25c', 'created_at': '2023-02-20 14:24:01.871499', '__class__': 'BaseModel'}"

        self.assertEqual(
            my_model_json, "{'my_number': 89, 'name': 'My First Model', 'updated_at': '2023-02-20 14:24:01.871493', 'id': '853d2737-0bc7-4dbe-a403-b3934a3de25c', 'created_at': '2023-02-20 14:24:01.871499', '__class__': 'BaseModel'}")

    

    def test_str(self):
        base_model = BaseModel()
        base_model.name = "John"
        base_model.save()
        expected_str = "[BaseModel] ({}) {}".format(
            base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

    def test_save(self):

        my_model = BaseModel()
        my_model.name = "John"

    
        my_model.save()
    
        with open('file.json', 'r') as f:
            content = json.load(f)
            key = "{}.{}".format(type(my_model).__name__, my_model.id)
            self.assertEqual(content[key]['name'], my_model.name)
