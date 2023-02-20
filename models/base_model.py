#!/usr/bin/python
import uuid
import datetime


class BaseModel:
    """
    A base model that provides an ID and timestamp for other models to inherit from.
    """

    def __init__(self, id=None, *args, **kwargs,):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            """
            Initializes a new instance of the BaseModel class.

            """

            if id is not None:
            	self.id = str(id) + ' - ' + str(uuid.uuid4())
            else:
            	self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def save(self):
        """
        Updates the timestamp for the model to the current date and time.
        """
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the model.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        Returns a dictionary representation of the model.
        """
        return {'id': self.id, 'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat(), '__class__': type(self).__name__}
