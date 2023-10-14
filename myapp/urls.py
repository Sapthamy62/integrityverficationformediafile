from . import views
from django.urls import path
urlpatterns = [
    path('',views.home),
    path('verify',views.verifyfile),
    path('about',views.about),
    path('login',views.loginaction),
    path('mediafiles',views.mediafile),
    # path('welcome',views.welcomeaction),
    path('upload',views.uploadfile),
    path('register',views.registeraction),
    #  path("action/<id>/", views.action, name ="article_detail"),
    #  path("disable/<id>/", views.disable, name ="article_detail")
    path('action/<int:id>/', views.action, name='action_d'),
    path('disable/<int:id>/', views.disable, name='disable_d')
]