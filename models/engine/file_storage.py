import json
import os
import models
"""
FileStorage Module
"""

class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Return __objects
        """
        if cls:
            temp_objs = {}
            for key, value in self.__objects.items():
                if (key.split(".")[0] == cls.__name__):
                    temp_objs.update({key: value})
            return temp_objs
        else:
            return self.__objects

    def new(self, obj):
        """
        Add obj to __objects
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to __file_path
        """
        temp_dict = {}
        for key, value in self.__objects.items():
            temp_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(temp_dict, file)

    def reload(self):
        """
        Deserialize __file-path to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                temp_dict = json.load(file)
            for key, value in temp_dict.items():
                temp_object = models.the_classes[value["__class__"]](**value)
                self.__objects[key] = temp_object

    def delete(self, obj=None):
        """
        Delete an object obj
        """
        if obj:
            for key, value in self.__objects.items():
                if value == obj:
                    del self.__objects[key]
                    self.save()
                    break

    def get(self, cls, id):
        """
        Returns the object based on the class and its ID
        """
        k = f"{cls.__name__}.{id}"
        for key, value in self.__objects.items():
            if key == k:
                return value
        return None

    def count(self, cls=None):
        """
        Count a class objects
        """
        return len(self.all(cls))
