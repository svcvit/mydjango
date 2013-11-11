#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *

urlpatterns = patterns(('myapp.views'),
    url(r'^bloglist/$', 'blog_list', name='bloglist'),
    url(r'^blog/(?P<id>\d+)/$', 'blog_show', name='detailblog'),
    # name属性是给这个url起个别名，可以在模版中引用而不用担心urls文件中url的修改 引用方式为{% url bloglist %}
)