from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resistance/<str:ticker>', views.resistance, name='resistance'),
    path('support/<str:ticker>', views.support, name='support'),
]
