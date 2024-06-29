"""
__init__ Module
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.category import Category
from models.course import Course


the_classes = {"BaseModel": BaseModel,
               "User": User,
               "Category": Category,
               "Course": Course}
storage = FileStorage()
storage.reload()
