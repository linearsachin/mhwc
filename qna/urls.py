from django.urls import path
from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('question/<slug>', views.QuestionView.as_view(), name='question'),
    path('generate_forum', views.generateForum, name='generate-forum'),
    path('forum-auth/<forum_id>', views.ForumAuthView.as_view(), name='forum-auth'),
    path('forum/<forum_id>/welcome', views.ForumView.as_view(), name='forum'),


]


