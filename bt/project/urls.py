from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('projectcreate/', ProjectCreateView.as_view(), name='projectcreate'),
    path('projectlist/', ProjectListView.as_view(), name='projectlist'),
    path('projectteamcreate/', ProjectTeamCreateView.as_view(), name='projectteamcreate'),
    path('projectteamlist/', ProjectTeamListView.as_view(), name='projectteamlist'),
    path('projectupdate/<int:pk>', ProjectUpdateView.as_view(), name='projectupdate'),
    path('projectdetail/<int:pk>', ProjectDetailView.as_view(), name='projectdetail'),
    path('projectdelete/<int:pk>', ProjectDeleteView.as_view(), name='projectdelete'),
]