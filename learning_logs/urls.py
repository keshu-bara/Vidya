"""Defines URL patterns for learning)logs."""
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #Home page
    path('',views.index,name='index'),
    path('Home/',views.index,name='index'),
    path('topics/',views.topics,name='topics'),
    path('topic/<int:topic_id>/',views.topic,name='topic'),
    path('newTopics/',views.newTopics,name='newTopics'),
    path('newEntry/<int:topic_id>',views.newEntry,name = 'newEntry'),
    path('editEntry/<int:entry_id>',views.editEntry,name = 'editEntry'),
    path('deleteEntry/<int:entry_id>',views.deletEntry,name='deletEntry'),
    path('deleteTopic/<int:topic_id>',views.deleteTopic,name='deleteTopic'),


]

