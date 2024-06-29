"""
User module
"""
from models import BaseModel


class User(BaseModel):
    """
    User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    phone = ""
    mentor_id = ""
