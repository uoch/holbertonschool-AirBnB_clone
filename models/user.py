#!/usr/bin/python3
"""user"""
from models.base_model import BaseModel
from models.engine.file_storage import update_filestorage


class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        return (f"[User]({self.id}) {self.__dict__}")


update_filestorage(User)
