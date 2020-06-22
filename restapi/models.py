from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User
)


class Project(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    repo = models.CharField(max_length=256, null=True)
    briefDesc = models.CharField(max_length=100, null=True)
    detailedDesc = models.CharField(max_length=300, null=True)
    categories = models.CharField(max_length=1000, null=True)
    technologies = models.CharField(max_length=1000, null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    # j'ajoute toujour ces deux attribut en cas de modification ou la suppression de données
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)

    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title


class Task (models.Model):
    #  id = models.IntegerField(max_length=200)
    title = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)
    date = models.DateField(max_length=500)
    project = models.ForeignKey(
        Project, null=False, default='1', on_delete=models.CASCADE)

    categories = models.CharField(max_length=1000, null=True)
    technologies = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.title


class Category (models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Technology (models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

  # -----------------------------------------------------------------


class UserDev(BaseUserManager):

    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):

        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


# class User(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)
#     admin = models.BooleanField(default=False)

#     objects = UserDev()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def get_full_name(self):

#         return self.email

#     def get_short_name(self):

#         return self.email

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):

#         return True

#     def has_module_perms(self, app_label):

#         return True

#     @property
#     def is_staff(self):
#         return self.staff

#     @property
#     def is_admin(self):
#         return self.admin

#     @property
#     def is_active(self):
#         return self.active


class list (models.Model):
    etats = (
        ('not started', 'not started'),
        ('in progress', 'in progress'),
        ('done', 'done'),
    )
    title = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)
    datedeb = models.DateField(max_length=500)
    datefin = models.DateField(max_length=500)
    etat = models.CharField(max_length=11, choices=etats)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    age = models.IntegerField()
    level = models.CharField(max_length=500)
    point = models.CharField(max_length=500)
    showEvents = models.BooleanField(default=True)
    showTDL = models.BooleanField(default=True)
    showALRM = models.BooleanField(default=True)
    isPublic = models.BooleanField(default=True)
    showLeaders = models.BooleanField(default=True)
    showStats = models.BooleanField(default=True)
    showRNDM = models.BooleanField(default=True)
    showActs = models.BooleanField(default=True)
    showNews = models.BooleanField(default=True)

    USER_TYPE_CHOICES = (
        (1, 'normal'),
        (2, 'developer'),
        (3, 'instructor'),
        (4, 'organization'),
    )

    userType = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username + " Profile"


class Forum(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title + " Discussion forum"


class ForumThread(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    body = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.title


class ThreadPost(models.Model):
    thread = models.ForeignKey(ForumThread, on_delete=models.CASCADE)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    body = models.CharField(max_length=1000, null=False)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title


class TaskContribution(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    PROGRESS_CHOICE = (
        (1, 'progress'),
        (2, 'validated'),
    )

    progress = models.PositiveSmallIntegerField(
        choices=PROGRESS_CHOICE)

    def __str__(self):
        return self.task.title + " <=> " + self.user.username


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    ACTIVITY_TYPE_CHOICES = (
        (1, 'project'),
        (2, 'forum'),
        (3, 'registered'),
        (4, 'contributed'),
    )

    activityType = models.PositiveSmallIntegerField(
        choices=ACTIVITY_TYPE_CHOICES)

    def __str__(self):
        return self.title
