from django.contrib import admin


from .models import Task
from .models import Project
from .models import Technology
from .models import Category
from .models import User
from .models import Profile
from .models import Forum
from .models import ForumThread
from .models import ThreadPost
from .models import TaskContribution
from .models import Activity

from .models import list
#from .models import Projet


# Register your models here.

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Category)

admin.site.register(list)
admin.site.register(Profile)

admin.site.register(Forum)
admin.site.register(ForumThread)
admin.site.register(ThreadPost)
admin.site.register(TaskContribution)
admin.site.register(Activity)
