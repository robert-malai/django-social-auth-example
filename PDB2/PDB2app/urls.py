from rest_framework import routers
from .views import ProjectsViewSet, UserViewSet

# urlpatterns = [
#     url(r'^$', views.ArtistList.as_view()),
#     url(r'^music/artist/$', views.ArtistList.as_view()),
#     url(r'^music/albums/$', views.AlbumList.as_view()),
#     url(r'^music/songs/$', views.SongList.as_view())
# ]

router = routers.DefaultRouter()
router.register(r'projects', ProjectsViewSet)
router.register(r'users', UserViewSet)
#router.register(r'projects/(?P<project_id>.+)', ProjectsDetails)
#router.register(r'projects/(?P<project_id>)/', ProjectsViewSet)

urlpatterns = router.urls