from django.urls import path,include
from .views import EmpListView

urlpatterns =[
     path('list-view/',EmpListView.as_view(),name='list_view')   
]

