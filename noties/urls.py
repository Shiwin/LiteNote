from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'lite_note.views.home', name='home'),
                       url(r'^test','lite_note.views.new_home',name='new_home'),
                       url(r'^note/(?P<id>[0-9]+)/', 'lite_note.views.note', name='note'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/',  views.login,  name='login'),
                       url(r'^logout/', views.logout,  {'next_page':  'home'},  name='logout'),
                       url(r'^register/',  'regsiter.views.registration', name='registration_register'),
                       url(r'^create/', 'lite_note.views.create_note', name='create_note'),
                       url(r'^unknown/', 'lite_note.views.enter_anonymous_user', name='enter_anonymous'),

                       url(r'^request_login','regsiter.views.request_login'),
                       url(r'^test','lite_note.views.new_home',name='new_home'),
)
