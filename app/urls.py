from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import login_view 
from views import logout_view 
from views import register_view 

from views import resume_view 

from views import skill_view 
from views import skill_edit_view 
from views import skill_delete_view

from views import exp_view 
from views import exp_edit_view 
from views import exp_delete_view 

from views import edu_view 
from views import edu_edit_view 
from views import edu_delete_view 

from views import lang_view 
from views import lang_edit_view 
from views import lang_delete_view 

from views import index_view

urlpatterns = patterns('',

    url(r'^$', index_view),
    url(r'^login/$', login_view, name = 'login'),
    url(r'^logout/$', logout_view, name = 'logout'),
    url(r'^register/$', register_view, name = 'register'),
    
    url(r'^resume/$', resume_view, name = 'resume'),
    
    url(r'^skills/$', skill_view, name = 'skill'),
    url(r'^skills/(?P<id>\d)/edit', skill_edit_view, name = 'skill_edit'),
    url(r'^skills/(?P<id>\d)/delete$', skill_delete_view, name = 'skill_delete'),
    
    url(r'^experience/$', exp_view, name = 'exp'),
    url(r'^experience/(?P<id>\d)/edit', exp_edit_view, name = 'exp_edit'),
    url(r'^experience/(?P<id>\d)/delete$', exp_delete_view, name = 'exp_delete'),
    
    url(r'^education/$', edu_view, name = 'edu'),
    url(r'^education/(?P<id>\d)/edit', edu_edit_view, name = 'edu_edit'),
    url(r'^education/(?P<id>\d)/delete$', edu_delete_view, name = 'edu_delete'),
    
    url(r'^languages/$', lang_view, name = 'lang'),
    url(r'^languages/(?P<id>\d)/edit', lang_edit_view, name = 'lang_edit'),
    url(r'^languages/(?P<id>\d)/delete$', lang_delete_view, name = 'lang_delete'),
)
