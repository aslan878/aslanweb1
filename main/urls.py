from django.urls import path
from . import views
urlpatterns = [
    path('',views.ind),
    path('about',views.about),
    path('eshe',views.eshe)
]