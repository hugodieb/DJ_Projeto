#encoding: utf-8

from django.conf.urls import patterns, include, url
from projects import views

urlpatterns = patterns('',
    
    url(r'^novo/$', views.CreateProject,
       name='projects_create' ),
    url(r'^view/$', views.ViewPerson,
        name='view_person'),
    url(r'^edit/$', views.EditPerson,
        name='edit_person'),
    url(r'^lista/$', views.ListProjects,
       name='projects_list' ),
    url(r'^edit/(?P<pk>\d+)$', views.UpdateProject,
    	name='project_edit'),
    url(r'^remove/(?P<pk>\d+)$', views.RemoveProject,
    	name='project_remove'),
    url(r'^search/$', views.SearchProject,
    	name='project_search'),
    url(r'^register/$', views.Register_user,
        name='user_register'),
    url(r'^login/$', views.Login_user,
        name='user_login'),
    url(r'^logout/$', views.Logout_user,
        name='user_logout'),

)
