from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from .models import Task
from .models import Category
from .models import Technology
from .models import Project
from .models import User
from .models import Profile
from .models import Forum
from .models import ThreadPost
from .models import ForumThread
from .models import TaskContribution
from .models import Activity

from .models import list

from django.core import serializers

from .serializer import TaskSerializer
from .serializer import CategorySerializer
from .serializer import TechnologySerializer
from .serializer import ProjectSerializer
from .serializer import UserSerializer
from .serializer import CUserSerializer
from .serializer import ProfileSerializer
from .serializer import ForumSerializer
from .serializer import ThreadSerializer
from .serializer import ThreadPostSerializer
from .serializer import TaskContributionSerializer
from .serializer import ActivitySerializer

# from .Forms import ProductForm
# from rest_framework import ProductForm
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.request import Request


from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes


from django.contrib.auth import authenticate, login

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.
# def list_product(request):
# p=Blogger.object.all()
# return render(request,'products.html',{'p':p})


from django.contrib.auth import authenticate, login


@csrf_protect
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):

        if self.request.GET.get('q') != None:
            return Task.objects.filter(Q(title__icontains=self.request.GET.get('q')) | Q(desc__icontains=self.request.GET.get('q')))
        else:
            return Task.objects.all()

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        frequency = Frequency.objects.get(id=pk)
        serializer = FrequencySerializer(frequency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [AllowAny]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.GET.get('id') != None:
            return Project.objects.filter(owner=self.request.GET.get('id'))
        elif self.request.GET.get('q') != None:
            return Project.objects.filter(Q(title__icontains=self.request.GET.get('q')) | Q(briefDesc__icontains=self.request.GET.get('q')) | Q(detailedDesc=self.request.GET.get('q')) | Q(categories__icontains=self.request.GET.get('q')))
        else:
            return Project.objects.all()

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        frequency = Frequency.objects.get(id=pk)
        serializer = FrequencySerializer(frequency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = list.objects.all()
    serializer_class = UserSerializer


class TestViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    queryset = Technology.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def test(request):
    return Response(data="serializer.data", status=status.HTTP_200_OK)


class current_profile(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class my_Projects(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def isAdmin(request):
    response = False
    if request.user.is_superuser:
        response = True
    return Response(data=str(response), status=status.HTTP_200_OK)


class ForumView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

    def get_queryset(self):
        if self.request.GET.get('proj') == None:
            return Forum.objects.all()
        else:
            return Forum.objects.filter(project=self.request.GET.get('proj'))


class ThreadView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    queryset = ForumThread.objects.all()
    serializer_class = ThreadSerializer

    def get_queryset(self):
        if self.request.GET.get('forum') != None:
            return ForumThread.objects.filter(forum=self.request.GET.get('forum'))
        elif self.request.GET.get('id') != None:
            return ForumThread.objects.filter(id=self.request.GET.get('id'))
        elif self.request.GET.get('q') != None:
            return ForumThread.objects.filter(Q(title__icontains=self.request.GET.get('q')) | Q(body__icontains=self.request.GET.get('q')))
        else:
            return ForumThread.objects.all()


class ThreadPostsView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = ThreadPost.objects.all()
    serializer_class = ThreadPostSerializer

    def get_queryset(self):
        if self.request.GET.get('p') != None:
            return ThreadPost.objects.filter(poster=self.request.GET.get('p'))
        elif self.request.GET.get('th') != None:
            return ThreadPost.objects.filter(thread=self.request.GET.get('th'))
        else:
            return ThreadPost.objects.all()


class ProfilesView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        if self.request.GET.get('id') == None:
            return Profile.objects.all()
        else:
            return Profile.objects.filter(user=self.request.GET.get('id'))


class TaskContribView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    queryset = TaskContribution.objects.all()
    serializer_class = TaskContributionSerializer

    def get_queryset(self):
        print(self.request.GET.get('id'))
        if self.request.GET.get('id') != None:
            return TaskContribution.objects.filter(task=self.request.GET.get('id'))
        elif self.request.GET.get('uid') != None:
            return TaskContribution.objects.filter(user=self.request.GET.get('uid'))
        else:
            return TaskContribution.objects.all()


class ActivityView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):

        if self.request.GET.get('uid') != None:
            return Activity.objects.filter(user=self.request.GET.get('uid'))
        elif self.request.GET.get('act') != None:
            return Activity.objects.filter(Q(activityType=1) | Q(activityType=4))
        else:
            return Activity.objects.all()
