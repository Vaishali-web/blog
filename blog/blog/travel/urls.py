
from django.urls import path,include
from .views import HomeView,EntryView,CreateEntryView

urlpatterns = [
    path('',HomeView.as_view(),name='blog-home'),
    path('entry/<int:pk>/',EntryView.as_view(),name='blog-travel-detail'),
    path('create_entry/',CreateEntryView.as_view(success_url='/'),name='blog-create-entry')
   
]