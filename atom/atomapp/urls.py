from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name="index"),
    url(r'^home/$', views.index , name="home"),
    url(r'^login/$', views.login , name="login"),
    url(r'^signup/$', views.signup , name="signup"),
    url(r'^myprofile/$', views.myprofile , name="myprofile"),
    url(r'^myprofile/logout/$', views.logout_view , name="logout_view"),
    url(r'^students/$', views.students_view , name="students"),
]
