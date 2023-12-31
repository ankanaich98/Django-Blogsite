from django.urls import path
from .import views

urlpatterns=[
    path('blog/', views.index , name='blog-index'),
    path('post_detail/<int:pk>/', views.post_detail , name='blog-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit , name='blog-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete , name='blog-post-delete'),
    path('new_post/', views.newPost , name='new-post'),
    path('approve_post/', views.approvePost , name='approve-post'),
    path('approve_post_detail/<int:pk>/', views.approve_post_detail , name='approve-post-detail'),
    path('my_posts/', views.my_posts , name='my-posts'),

]