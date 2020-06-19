from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('question/<slug>', views.QuestionView.as_view(), name='question'),
    path('generate_forum', views.generateForum, name='generate-forum'),
    # path('forum-auth/<forum_id>', views.ForumAuthView.as_view(), name='forum-auth'),
    path('forum/<forum_id>/welcome', views.ForumView.as_view(), name='forum'),
    path('about', views.AboutView.as_view(), name='about'),
    path('forum-auth/', auth_views.LoginView.as_view(template_name='qna/forum-auth.html'),name='forum-auth'),
    path('forum-out/', auth_views.LogoutView.as_view(template_name='qna/forum-out.html'),name='forum-out'),



]


