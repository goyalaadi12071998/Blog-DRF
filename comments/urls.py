from django.urls import path
from .views import comment_list
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('blogs/<int:pk>/comments', comment_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
