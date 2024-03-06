from django.contrib import admin
from django.urls import include, path

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>', views.category_posts,
         name='category_posts'),
    path('pages/', include('pages.urls')),
]
