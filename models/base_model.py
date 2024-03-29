#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    def __init__(self, *args, **kwargs):
        """
        Args:
            *args: Constructor of BaseModel set to "None"
            **kwargs: Constructor of BaseModel
        """
        if kwargs:
            excluded_keys = {"__class__", "created_at", "updated_at"}
            for key in kwargs:
                if key not in excluded_keys:
                    setattr(self, key, kwargs[key])
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(kwargs[key], DATE_FORMAT))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return the following objects:
            - class name: in format [BaseModel]
            - id: to hold the unique class identifier
            - created_at: date object is created
            - updated_at: date object is updated
        """
        return '[{}] ({}) {}'.format(class_name, uuid, class_dict)

    def save(self):
        """Save updated_at anytime this function is called."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing key and value of the instance
        including class name.
        """
        result_dict = {key: value for key, value in self.__dict__.items() if key not in ["created_at", "updated_at"]}
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        result_dict['__class__'] = self.__class__.__name__
        return result_dict
