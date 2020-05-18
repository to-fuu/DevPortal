from django.db import models


class Project(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    repo = models.CharField(max_length=256, null=True)
    briefDesc = models.CharField(max_length=100, null=True)
    detailedDesc = models.CharField(max_length=300, null=True)
    categories = models.CharField(max_length=1000, null=True)
    technologies = models.CharField(max_length=1000, null=True)

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
