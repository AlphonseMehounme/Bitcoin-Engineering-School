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

    def all(self):
        """
        Return __objects
        """
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
