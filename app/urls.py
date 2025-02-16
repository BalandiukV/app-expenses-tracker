from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(
        [
            path('expenses/', include('expenses.urls')),
            path('users/', include('users.urls')),
        ]
    )),
]
