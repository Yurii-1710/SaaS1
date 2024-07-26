
from django import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('visits.urls')),
    path('auth/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
]
