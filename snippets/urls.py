from django.conf.urls import url, include
from snippets.views import SnippetViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^/api/', include(router.urls)),
]
