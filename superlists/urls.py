from django.conf.urls import url

from lists import views

urlpatterns = [
	url(r'^$', views.home_page, name='home'),
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
]
