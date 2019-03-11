from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(r'', views.PostListView.as_view(), name='post_list'),
    path(r'<int:year>/<int:month>/<int:day>/<slug:post>',
         views.post_detail,
         name='post_detail'),
]