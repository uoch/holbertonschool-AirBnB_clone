#!/usr/bin/python3
import uuid
import datetime
import models


class BaseModel:
    """
    A base model that provides an ID
    and timestamp for other models to inherit from.
    """

    def __init__(self, id=None, created_at=None, updated_at=None, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'id':
                        self.id = value
                    elif key == 'created_at':
                        self.created_at = datetime.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    elif key == 'updated_at':
                        self.updated_at = datetime.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
            if 'id' not in kwargs:
                self.id = id or str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.datetime.now()
        else:
            self.id = id or str(uuid.uuid4())
            self.created_at = created_at or datetime.datetime.now()
            self.updated_at = updated_at or datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Updates the timestamp for the model to the current date and time.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def __str__(self):
        """
        Returns a string representation of the model.
        """
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        Returns a dictionary representation of the model.
        """
        return {'id': getattr(self, 'id', None),
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat(),
                '__class__': type(self).__name__}
