"""
__init__ Module
"""
from .engine import file_storage
from models.base_model import BaseModel


the_classes = {"BaseModel": BaseModel}
storage = file_storage.FileStorage()
storage.reload()
