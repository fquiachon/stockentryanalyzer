from rest_framework import routers
from .api import UserViewSet
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', include(router.urls)),
    path('resistance/<str:ticker>', views.ResistanceView.as_view(), name='resistance'),
    path('support/<str:ticker>', views.SupportView.as_view(), name='support'),
    path('resistance', views.ResistanceView.as_view(), name='resistances'),
    path('support', views.SupportView.as_view(), name='supports'),
]
