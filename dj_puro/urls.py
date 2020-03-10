from django.urls import path
from dj_puro.views import category_list, category_detail

app_name = 'category'

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categories/<int:pk>', category_detail, name='category_detail'),
]
