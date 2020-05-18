

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from restapi.views import TaskViewSet
from restapi.views import ProjectViewSet
from restapi.views import TechnologyViewSet
from restapi.views import CategoryViewSet

from rest_framework import viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)
router.register('projects', ProjectViewSet)
router.register('categories', CategoryViewSet)
router.register('technologies', TechnologyViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    path('admin/', admin.site.urls)
]
