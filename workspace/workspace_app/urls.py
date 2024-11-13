from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='workspace'),
    path('sign', views.sign_view, name='sign')
]