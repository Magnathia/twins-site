from django.urls import path
from . import views


app_name = 'home'  # done for namespacing URLs.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("wsu/", views.wsu, name="wsu_ethan"),
    path("harvard/", views.harvard, name="harvard_ethan"),
    path("bellevue/", views.bellevue, name="bellevue_eric"),
    path("caltech/", views.caltech, name="caltech"),
    path("about/", views.about, name="about"),

]