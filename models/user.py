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
    phone = 98
    mentor_id = ""
