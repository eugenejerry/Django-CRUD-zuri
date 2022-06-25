from dataclasses import fields
import imp  # did not import this
from pyexpat import model  # did not import this
from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
# def index(response):
#     return HttpResponse("Hello, This is my first View")

######## my created class views ##########


class PostListView(ListView):
    model = Post
    template_name = "home.html"


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


