from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from manytomany.views import PropertyViewSet

router = routers.DefaultRouter()
router.register(r'properties', PropertyViewSet)


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/auth/token/',
        'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
)
