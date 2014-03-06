#encoding: utf-8

from django.conf.urls import patterns, include, url
from .views import CreateProjectView, ListProjects, UpdateProject, RemoveProject, SearchProject, Register_user

urlpatterns = patterns('',
    
    url(r'^novo/$', CreateProjectView.as_view(),
       name='projects_create' ),
    url(r'^lista/$', ListProjects.as_view(),
       name='projects_list' ),
    url(r'^edit/(?P<pk>\d+)$', UpdateProject,
    	name='project_edit'),
    url(r'^remove/(?P<pk>\d+)$', RemoveProject,
    	name='project_remove'),
    url(r'^search/$', SearchProject,
    	name='project_search'),
    url(r'^register/$', Register_user,
        name='user_register'),

)
