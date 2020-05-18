from rest_framework import serializers
from .models import Task
from .models import Category
from .models import Technology
from .models import Project


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'title', 'desc', 'date',
                  'project', 'categories', 'technologies']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'repo', 'title', 'briefDesc',
                  'detailedDesc', 'createdAt', 'updatedAt', 'categories']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name']


class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technology
        fields = ['url', 'name']
