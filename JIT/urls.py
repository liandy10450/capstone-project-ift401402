from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.vendor, name='vendor'),
    #path('', views.receiving, name='receiving'),
    url(r'^vendor/$',views.vendor, name="vendor"),
    url(r'^receiving/$',views.receiving, name="receiving"),
    url(r'^$',views.index),
    #path('post/new/', views.process, name='process_selected'),
    url(r'^create/$', views.order_create, name="order_create"),
    path('CRUD_template/' , views.CRUD_template, name="CRUD_template"),
    #path('post/new/', views.post_new, name='post_new'),
    path('update/<str:pk>/' , views.order_update, name="order_update"),
    path('delete/<str:pk>/' , views.order_delete, name="order_delete"),
]

