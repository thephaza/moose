from django.contrib import admin
from django.urls import path
from .views import home_view, blog_view, about_view, contact_view, blog_detail_view, tag_view, all_view


urlpatterns = [
    path('', home_view),
    path('blog/', blog_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('blog/<int:pk>/', blog_detail_view),
    path('tag/<int:pk>/', tag_view),
    path('all-blogs/',all_view)

]
