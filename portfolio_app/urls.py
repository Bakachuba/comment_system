from django.urls import path
from .views import post_detailview

urlpatterns = [

    path('post/<int:id>/', post_detailview, name='post_detail'),
]
