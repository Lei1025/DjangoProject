##lab5 group2 pangfan 104439988 liulei 104651816

from django.conf.urls import url
from myapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/$',views.about, name='about'),
        url(r'^(?P<course_No>\d+)/$', views.detail, name='detail'),
        url(r'^addtopic/$',views.addtopic, name='addtopic'),
        url(r'^topics/$',views.topics, name='topics'),
        url(r'^topics/(?P<topic_id>.*)/$', views.topicdetail, name='topicdetail'),
        url(r'^register/$',views.register,name='register'),
        url(r'^login/$',views.user_login, name='login'),
        url(r'^logout/$',views.user_logout,name='logout'),
        url(r'^mycourse/$', views.mycourse, name='mycourse'),
        url(r'^forgetpasswork/$', views.fotgetPassword, name= 'forgetpassword')

]
