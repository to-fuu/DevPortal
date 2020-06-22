

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from restapi.views import TaskViewSet
from restapi.views import ProjectViewSet
from restapi.views import TechnologyViewSet
from restapi.views import CategoryViewSet
from restapi.views import current_profile, TestViewset, my_Projects
from restapi.views import test, login_view, isAdmin, ForumView, ThreadView, ProfilesView, TaskContribView, ActivityView, ThreadPostsView


from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework import viewsets
from django.conf import settings
from django.conf.urls.static import static


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email',
                  'is_staff', 'first_name', 'last_name', 'pk']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):

        if self.request.GET.get('q') != None:
            return User.objects.filter(username__icontains=self.request.GET.get('q'))
        else:
            return User.objects.all()


router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)
router.register('projects', ProjectViewSet)
router.register('categories', CategoryViewSet)
router.register('technologies', TechnologyViewSet)
router.register('testtest', TestViewset)
router.register('profile', current_profile)
router.register('profiles', ProfilesView)
router.register('my_projects', my_Projects)
router.register('forums', ForumView)
router.register('threads', ThreadView)
router.register('threads', ThreadView)
router.register('taskcontrib', TaskContribView)
router.register('activities', ActivityView)
router.register('threadPosts', ThreadPostsView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    path('admin/', admin.site.urls),
    path('test/', test, name="test"),
    path('auth/', include('authapp.urls')),
    path('auth/login', login_view, name="login_view"),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/user/isAdmin', isAdmin, name="IsAdmin"),

    # url(r'^rest-auth/user/profile', current_profile, name="profile")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
