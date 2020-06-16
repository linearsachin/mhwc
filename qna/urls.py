from django.urls import path
from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('question/<slug>', views.QuestionView.as_view(), name='question'),
    path('search', views.search, name='search'),
]


