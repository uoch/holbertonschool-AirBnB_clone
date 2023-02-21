#!/usr/bin/python3
import unittest
from base_model import BaseModel


class Test_Base_Model(unittest.TestCase):
    def setUp(self):
        self.base_model = Base_Model()

    def test_has_id(self):
        self.assertTrue(hasattr(self.base_model, 'id'))

    def test_has_created_at(self):
        self.assertTrue(hasattr(self.base_model, 'created_at'))

    def test_has_updated_at(self):
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        before_save = self.base_model.updated_at
        self.base_model.save()
        after_save = self.base_model.updated_at
        self.assertGreater(after_save, before_save)

    def test_to_dict_returns_dict(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_has_correct_keys(self):
        model_dict = self.base_model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(model_dict.keys(), expected_keys)

    def test_to_dict_has_correct_class(self):
        model_dict = self.base_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'Base_Model')


if __name__ == '__main__':
    unittest.main()
