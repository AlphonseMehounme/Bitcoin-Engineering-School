"""
__init__ Module
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


the_classes = {"BaseModel": BaseModel, "User": User}
storage = FileStorage()
storage.reload()
