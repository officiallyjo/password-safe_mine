from django.urls import path

from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('<int:pk>', views.detail,name='details'),
    path('add/',views.add , name ='add'),
    path('update/<int:pk>',views.update, name='update'),
    path('delete/<int:pk>',views.delete,name= 'delete')
    ]
