from django.urls import path
from .views import Students_API
urlpatterns = [
    path('', Students_API.as_view()),
    path('<str:reg_no>/', Students_API.as_view())   
]