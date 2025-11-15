from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('add-topic/', views.add_topic_view, name='add_topic'),
    path('toggle-status/<int:topic_id>/', views.toggle_status_view, name='toggle_status'),
    path('delete-topic/<int:topic_id>/', views.delete_topic_view, name='delete_topic'),
]
