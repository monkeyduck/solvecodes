from django.conf.urls import patterns, include, url

from django.contrib import admin
from login.views import register,mylogin,mylogout,homepage,changepassword
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyLogin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^register/$',register),
    (r'^login/$',mylogin),
    (r'^home/$',homepage),
    (r'^logout/$',mylogout),
    (r'^login/register/$',register),
    (r'^changepassword/(?P<username>\w+)/$',changepassword),
)
