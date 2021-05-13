from django.urls import path
from . import views
app_name="pages"
urlpatterns = [
    #path("",views.HomePageView.as_view(),name="home"),
    path("",views.home,name="home"),
    path("create_post/",views.create_post,name="create_post"),
    path("post/",views.post,name="post"),
]
