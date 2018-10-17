from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.welcome, name = 'welcome'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^post_project/$', views.post_project, name='post_project'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^search/$', views.search_results, name = 'search_results'),
    url(r'^projects/(\d+)/',views.each_project,name='each_project'),

    url(r'^api/proj/$', views.ProjectList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
