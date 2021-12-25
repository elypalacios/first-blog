from re import template
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.utils import timezone

from blog.serializers import PostSerializer
from blog.models import Post
#from blog.models import Book 

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html', {'posts':posts})



#def Post(request):
  #post_list = post.object.order_by ('-pub_date')[:5]
  #output = ',' .join([])
  #RetrieveUpdateAPIView
  #return HttpResponse