# filepath: c:\Users\User\Desktop\projectmanage\task_management_api\urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Include the tasks app URLs
]