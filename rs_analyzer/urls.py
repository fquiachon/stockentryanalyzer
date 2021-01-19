from rest_framework import routers
from . import views
from django.urls import path, include
from .viewsets import UserViewSet, SupportViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('lows', SupportViewSet, 'lows')

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', include(router.urls)),
    path('global/resistance', views.ResistanceView.as_view(), name='resistance'),
    path('global/support', views.SupportView.as_view(), name='support'),
    path('global/resistance/<str:ticker>', views.ResistanceView.as_view(), name='resistance'),
    path('global/support/<str:ticker>', views.SupportView.as_view(), name='support'),

    path('pse/resistance', views.PSEResistanceView.as_view(), name='pse_resistance'),
    path('pse/support', views.PSESupportView.as_view(), name='pse_support'),
    path('pse/resistance/<str:ticker>', views.PSEResistanceView.as_view(), name='pse_resistance'),
    path('pse/support/<str:ticker>', views.PSESupportView.as_view(), name='pse_support')
]
