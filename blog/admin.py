# blog/admin.py
# error message when pressing the save button_no table found is the error

from django.contrib import admin
from .models import Post

admin.site.register(Post)