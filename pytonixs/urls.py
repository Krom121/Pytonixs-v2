from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from pages.views import AboutView, ContactUsView, HomeView, ProjectView, ServiceView, ContactView
from blog.views import PostListView, PostDetailView
from rest_framework import routers, serializers, viewsets
from rest01.views import (PostList, PostDetail, 
        CreatePost, UpdatePost, DeletePost
)

urlpatterns = [
    path('batmans-admin/', admin.site.urls),
    ### PAGES APP URLS ###
    path('', HomeView.as_view(), name='home'),
    path('about_us/', AboutView.as_view(), name='about'),
    path('what_we_do/', ServiceView.as_view(), name='service'),
    path('completed_projects/', ProjectView.as_view(), name='project'),
    path('contact_us/', ContactUsView.as_view(), name='contact'),
    #### BLOG URLS ###
    path('blog', PostListView.as_view(), name='list'),
    path('post/<slug>/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/', PostList.as_view(), name='post-list'),
    path('post/<slug>/<pk>/', PostDetail.as_view(), name='post-detail' ),
    path('post/create', CreatePost.as_view(), name='create-post'),
    path('post/<pk>/update', UpdatePost.as_view(), name='update-post'),
    path('post/<pk>/delete', DeletePost.as_view(), name='delete-post'),
    ## OTHER BASE URLS FOR DEPENDENCIES #####
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
