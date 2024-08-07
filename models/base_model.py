"""
Base model module
"""
from datetime import datetime
import models
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        BaseModel Class
        """
        if kwargs:
            iso_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(value, iso_format)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Custom str method
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Method to save an object
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dict format of an object
        """
        dict = self.__dict__.copy()
        dict["created_at"] = dict["created_at"].isoformat()
        dict["updated_at"] = dict["updated_at"].isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
