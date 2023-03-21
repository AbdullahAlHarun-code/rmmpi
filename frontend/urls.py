from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    #path('', views.page_404, name="page_404"),
    path('application-form', views.upload_cv, name="upload_cv"),
    # path('', views.index, name="home"),
    # path('application-form', views.upload_cv, name="upload_cv"),
]
