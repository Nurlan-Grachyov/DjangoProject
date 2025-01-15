from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),

    path('mymodel/create/', views.MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodel/list/', views.MyModelListView.as_view(), name='mymodel_list'),
]