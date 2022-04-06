from django.urls import path,include
from LibraryApp.api.views import LibraryList,LibraryDetail,all_events
from . import views

urlpatterns = [
    path('list/',LibraryList.as_view(),name='book-list'),
    path('<int:pk>/',LibraryDetail.as_view(),name='book-detail'),
]
