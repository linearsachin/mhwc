from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('public-question/<slug>', views.PublicQuestionView.as_view(), name='publicquestion'),
    path('question/<slug>', views.QuestionView.as_view(), name='question'),
    # path('generate_forum', views.generateForum, name='generate-forum'),
    # path('forum/welcome', views.ForumView.as_view(), name='forum'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('log-in/', auth_views.LoginView.as_view(template_name='qna/forum-auth.html'),name='forum-auth'),
    path('log-out/', auth_views.LogoutView.as_view(template_name='qna/forum-out.html'),name='forum-out'),
    path('blogs/', views.BlogLinksView.as_view(),name='blog-links'),
    path('blog/<blog_slug>', views.BlogView.as_view(),name='blog'),


]


