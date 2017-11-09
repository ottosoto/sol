from django.conf.urls import url
from muebles import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^producto/nuevo/$', views.producto_nuevo, name='producto_nuevo'),
    ]
