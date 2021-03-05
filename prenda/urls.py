from django.urls import path
from .views import ProductoView,ProductoUpdateView,ProductoDeleteView


urlpatterns = [ 

	path('',ProductoView.as_view(),name="proView"),
	path('producto/edit/<int:pk>/',ProductoUpdateView.as_view(),name="proUpdate"),
	path('producto/delete/<int:pk>/',ProductoDeleteView.as_view(),name="proDelete"),

]