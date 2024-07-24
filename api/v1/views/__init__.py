"""
views Package init file
"""
from flask import Blueprint

from . import *

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

"""
Import everything from modules
"""
from api.v1.views.categories import *
from api.v1.views.courses import *
from api.v1.views.users import  *
