from django.contrib import admin
from django.urls import path
from intaisima import views as local_views
from post import views as post_views

"""comentarios"""

urlpatterns = [
    path('hello_world/',local_views.hello_world),
    path('hi/<str:name>/<int:age>/',local_views.say_hi),
    path('posts',post_views.list_posts),
    ]
