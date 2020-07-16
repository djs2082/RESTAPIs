from django.urls import path
from .views import Corona_API
urlpatterns = [
    path('', Corona_API.as_view()),
    path('<str:user_state>/', Corona_API.as_view()),
    path('<str:user_state>/<str:user_district>/', Corona_API.as_view()),   
]