#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.category import Category
from models.course import Course

all_objs = storage.all(Course)
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

#storage.delete(my_user)

print("-- Create a new Category --")
my_category = Category()
my_category.name = "Simple Course"
my_category.save()
print(my_category)

storage.delete(my_category)

print("-- Create a new Course --")
my_course = Course()
my_course.name = "BitDev"
my_course.description = "A great course for Bitdevs"
my_course.save()
print(my_course)
