from django.urls import path
from . import views
from .views import UserFollowedDeleteView


urlpatterns = [

    path('', views.userfollows, name='userfollows-home'),
    path('<int:pk>/userfollowed-delete/', UserFollowedDeleteView.as_view(),
         name='userfollowed-delete'),
]

