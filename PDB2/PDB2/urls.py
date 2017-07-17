"""PDB2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from social_django.urls import urlpatterns as social_django_urls


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('PDB2app.urls'))
]

urlpatterns += [
    #url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^', include(social_django_urls, namespace='social'))
    #url(r'^', include(router.urls)),
    #url(r'^admin/', include(admin.site.urls)),
]