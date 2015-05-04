from django.conf.urls import include, url, patterns
from django.contrib import admin
from strangerLove import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'strangerLove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index')
]