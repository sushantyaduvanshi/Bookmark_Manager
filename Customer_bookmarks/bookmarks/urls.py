from django.urls import path
from .views import index, create_bookmark, browse_bookmark

urlpatterns = [
    path('', index, name='index page'),
    path('_api/create', create_bookmark, name='new bookmark'),
    path('_api/browse', browse_bookmark, name='browse bookmarks'),
]