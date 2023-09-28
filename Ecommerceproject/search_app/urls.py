from django.urls import path, include

from search_app import views

app_name='search_app'
urlpatterns = [
    path('',views.SearchResult,name='SearchResult'),
]
