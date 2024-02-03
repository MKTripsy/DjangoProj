from django.urls import path
from . import views
#
#
#
#        ;    ,
#         ,    .
#       .;   :
urlpatterns = [
    #All path here is for main page
    path ('', views.back, name='back'),
    path ('homepage', views.home, name='home'),
    path ('about', views.about, name='about'),
    
    #Inside of "EXPLORE"
    path ('explore', views.explore, name='explore'),
    
    path ('explore', views.backEx, name='backEx'),
    path ('floor1',views.floor1, name= 'floor1'),
    path ('floor2',views.floor2, name= 'floor2'),
    path ('floor3',views.floor3, name= 'floor3'),
    path ('floor4',views.floor4, name= 'floor4'),
    path ('floor5',views.floor5, name= 'floor5'),
    path ('floor6',views.floor6, name= 'floor6'),
    path ('floor7',views.floor7, name= 'floor7'),
    path ('overview',views.overview, name='overview'),
    
    
    #ABOUT US
    path ('tripolcaprofile', views.tripolca, name='tripolca'),
    path ('adorprofile', views.ador, name='ador'),
    path ('maravillaprofile', views.maravilla, name='maravilla'),
    
]
