from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),

    path('mymodel/create/', views.MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodel/list/', views.MyModelListView.as_view(), name='mymodel_list'),
    path('mymodel/detail/<int:pk>/', views.MyModelDetailView.as_view(), name='mymodel_detail'),
    path('mymodel/update/<int:pk>/', views.MyModelUpdateView.as_view(), name='mymodel_update'),
    path('mymodel/delete/<int:pk>/', views.MyModelDeleteView.as_view(), name='mymodel_delete'),
    path('student/create/', views.StudentCreateView.as_view(), name='student_create'),
]