from rest_framework import serializers
from .models import Task
from .models import Category
from .models import Technology
from .models import Project
from .models import User
from .models import Profile
from .models import Forum
from .models import ForumThread
from .models import ThreadPost
from .models import TaskContribution
from .models import Activity


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'id', 'title', 'desc', 'date',
                  'project', 'categories', 'technologies']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'owner', 'repo', 'title', 'briefDesc',
                  'detailedDesc', 'createdAt', 'updatedAt', 'categories', 'id']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name']


class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technology
        fields = ['url', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', "Date_joined"]


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'id', 'user', 'age', 'photo',
                  'level', 'point', 'userType', 'isPublic', 'showALRM',
                  'showTDL', "showEvents", 'showStats', "showLeaders",
                  'showALRM', 'showTDL', "showRNDM",  "showActs",
                  "showNews"]


class CUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ForumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forum
        fields = ['url', 'id', 'project']


class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ForumThread
        fields = ['url', 'id', 'forum', 'poster',
                  'title', 'createdAt', 'body']


class ThreadPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThreadPost
        fields = ['url', 'id', 'thread', 'poster',
                  'title', 'createdAt', 'body']


class TaskContributionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskContribution
        fields = ['url', 'id', 'user', 'task', 'updated', 'progress']


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['url', 'id', 'user', 'title', 'created', 'activityType']
