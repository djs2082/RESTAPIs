from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('corona/', include('corona.urls')),
    path('students/',include('students.urls')),
    path('gettoken/',views.obtain_auth_token,name='api-token-auth')
]