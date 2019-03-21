from django.conf.urls import url, include
from carride import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^myaccount/', views.MyAccount, name='myaccount'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^cardetails/(?P<model_slug>[\w\-]+)/', views.show_car_details, name='cardetails'),
    url(r'^sell/$', views.sell, name='sell'),
    url(r'^buy/', views.buy, name='buy'),
    url(r'^rent/$', views.rent, name='rent'),
    url(r'^compare/$', views.compare, name='compare'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^delete/', views.delete_account, name='delete_account'),
    url(r'^search/', views.search, name='search'),
    ]


