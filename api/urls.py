from django.urls import path
from api.views.demand import DemandCreateView, DemandListView, DemandUpdateView
from api.views.creator import CreatorCreateView, CreatorDetailView, CreatorListView
from api.views.video import VideoListView
from rest_framework.routers import DefaultRouter
from .views import index as views_index

app_name = "api"

router = DefaultRouter()
router.register(r'content-requests', DemandListView)
urlpatterns = [
    path("index", views_index.index, name="index"),
    path('demande/', DemandListView.as_view(), name='demand-list'),
    path('createur/', CreatorListView.as_view(), name='creator-list'),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path(
        "createur/<int:pk>/",
        CreatorDetailView.as_view(),
        name="createur_detail",
    ),

    path('demand/create/', DemandCreateView.as_view(), name='demand-create'),
    path('createur/create/', CreatorCreateView.as_view(), name='creator-create'),
    path('demand/<int:pk>/update/', DemandUpdateView.as_view(), name='demand-update'),
]
