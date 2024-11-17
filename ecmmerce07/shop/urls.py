from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('add_product/', views.add_product, name= "add_product"),
    path('edit_product/<int:pr0duct_id>/', views.edit_product, name= "edit_product"),
    path('delete_product/<int:pk>/', views.delete_product, name= "delete_product"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    #path('logout/', views.logout, name='logout'),
]