"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path #django 2.0以上版本
from django.conf.urls import url
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static


#from blog.views import post_list, post_detail
from blog.views import IndexView, CategoryView, TagView, PostDetailView,SearchView,AuthorView
from config.views import LinkListView
from comment.views import CommentView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$' , CategoryView.as_view() , name='category-list') ,
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name = 'post-detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^ckdeitor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', admin.site.urls, name='admin'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns = [
#     url(r'^$', post_list, name='index'),
#     url(r'^category/(?P<category_id>\d+)/$', post_list, name = 'category-list'),
#     url(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),
#     url(r'^post/(?P<post_id>\d+).html$', post_detail, name = 'post-detail'),
#     url(r'^links/$', links, name = 'links'),
#     url(r'^admin/', admin.site.urls, name='admin'),
# ]
