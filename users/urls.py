from django.urls import path
from .views import home, profile, RegisterView, CreateView 
from . import views 
urlpatterns = [
    path('/', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('create/', CreateView.as_view(), name='create-meeting'),
    path('meetings/', views.all_meetings, name='view-meeting'),
    path('profile/', profile, name='users-profile'),
    path('add_venue', views.add_venue, name= 'add-venue'),
    path('take_minutes/', views.take_minutes, name= 'take_minutes'),
]
