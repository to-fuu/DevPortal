from django.contrib import admin


from .models import Task
from .models import Project
from .models import Technology
from .models import Category

#from .models import Projet


# Register your models here.

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Category)
