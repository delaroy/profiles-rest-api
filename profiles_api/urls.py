from djanggo.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.asview()),
]
