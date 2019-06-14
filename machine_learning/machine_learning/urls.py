from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('code1/', views.info),
]
