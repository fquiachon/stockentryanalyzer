from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('v1/', include('rs_analyzer.urls')),
    path('admin/', admin.site.urls),
]
