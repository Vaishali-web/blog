
from django.urls import path,include
from .views import HomeView,EntryView,CreateEntryView,PostDeleteView,PostUpdateView,CommentCreate
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/',HomeView.as_view(),name='blog-home'),
    path('entry/<int:pk>/',EntryView.as_view(),name='blog-travel-detail'),
    path('create_entry/',CreateEntryView.as_view(success_url='/'),name='blog-create-entry'),
    path('',views.home,name="home"),
    path('entry/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('entry/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path("profile/", views.profile, name="profile"),
    path('entry/<int:pk>/comment/',CommentCreate.as_view(),name='create_comment'),
]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

