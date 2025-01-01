from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('auth/', include("authen.urls")),
    path('custom_admin/', include("adminpanel.urls")),
    
]
