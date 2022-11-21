from django.urls import path
from . import views
 
urlpatterns = [ 
path('', views.index, name='index'),
path('login', views.log, name='login'),
path('registro', views.registro, name='registro'),
path('productos',views.productos,name='productos'),
path('crudproductos',views.crudproductos,name='crudproductos'),
path('compras',views.compras,name='compras'),
path('crudcompras',views.crudcompras,name="crudcompras"),
path('modcompras/<id>/',views.modcompras,name="modcompras"),
path('deletecompras/<id>/',views.deletecompras,name="deletecompras"),
path('modproductos/<id>/',views.modproductos,name="modproductos"),
path('deleteproductos/<id>/',views.deleteproductos,name="deleteproductos"),
] 