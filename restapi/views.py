from django.shortcuts import render, redirect

from .models import Task
from .models import Category
from .models import Technology
from .models import Project

from .serializer import TaskSerializer
from .serializer import CategorySerializer
from .serializer import TechnologySerializer
from .serializer import ProjectSerializer

# from .Forms import ProductForm
# from rest_framework import ProductForm
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# def list_product(request):
# p=Blogger.object.all()
# return render(request,'products.html',{'p':p})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

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


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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
