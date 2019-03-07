from django.conf.urls import url
from carride import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^myaccount/', views.MyAccount, name='myaccount'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^cardetails/(?P<model_slug>[\w\-]+)/$', views.show_car_details, name='cardetails'),
    url(r'^sell/$', views.sell, name='sell'),
    ]


