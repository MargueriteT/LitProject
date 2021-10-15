from django.urls import path
from . import views
from .views import TicketDeleteView, ReviewDeleteView, \
    ReviewUpdateView, TicketUpdateView, ReviewDetailView, \
    TicketDetailView


urlpatterns = [

    path('', views.home, name='blog-home'),
    path('user_posts/', views.user_posts, name='user_posts'),
    path('<int:pk>/review-detail/', ReviewDetailView.as_view(),
         name='review-detail'),
    path('<int:pk>/ticket-detail/', TicketDetailView.as_view(),
         name='ticket-detail'),
    path('<int:pk>/ticket-delete/', TicketDeleteView.as_view(),
         name='ticket-post-delete'),
    path('<int:pk>/review-delete/', ReviewDeleteView.as_view(),
         name='review-post-delete'),
    path('<int:pk>/review-update/', ReviewUpdateView.as_view(),
         name='review-post-update'),
    path('<int:pk>/ticket-update/', TicketUpdateView.as_view(),
         name='ticket-post-update'),
    path('new_review/', views.ReviewCreateView,
         name='new_review'),
    path('new_ticket/', views.TicketCreateView, name='ticket-create'),
    path('<int:pk>/review/', views.ResponseCreateReview,
         name='response-review'),
]
