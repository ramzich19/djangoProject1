"""djangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from game.views import contact
from core import views
from core.views import IndexList
from core.views import oferta
from core.views import Search
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexList.as_view(), name='index'),
    path('oferta', oferta, name = "oferta"),
    path('rep', include('core.urls')),
    path('topback/', include('game.urls')),
    path('', include('authapp.urls')),
    path('contact/', contact, name = "contact"),
    path('i18n/', include('django.conf.urls.i18n')),
    path('search/', Search.as_view(), name='search'),
    path('projects/', include('cores.urls')),
]

urlpatterns += i18n_patterns(
    path('', IndexList.as_view(), name='index'),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include("core.urls")),
    path('', include("cores.urls")),
    path('', include('authapp.urls')),
    path('topback/', include('game.urls')),
    path('projects/', include('cores.urls')),


)
if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
