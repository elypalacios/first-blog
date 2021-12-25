from django.urls import include, path
from rest_framework import routers 
from . import views
from blog.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('post_list', views.post_list, name='post_list'),
 # path('book', views.post_list, name='post_list')
 # path('home')
]


 #urls py call endpoint add another path ex: homeppage
 # local host create a route use a different end point ( simpler to post) how to make the connect
# introduce in blog/url.py under blog and intoduce it views.py 