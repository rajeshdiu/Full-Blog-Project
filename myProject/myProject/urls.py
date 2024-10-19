
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("", signupPage, name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("homePage/", homePage, name="homePage"),
    path("addBlogPage/", addBlogPage, name="addBlogPage"),
    path("createdBlogBy/", createdBlogBy, name="createdBlogBy"),
    path("ProfilePage/", ProfilePage, name="ProfilePage"),
    path("AllBlogPost/", AllBlogPost, name="AllBlogPost"),
    path("search_blog/", search_blog, name="search_blog"),
    
    
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("editBlog/<str:blog_id>", editBlog, name="editBlog"),
    path("deleteBlog/<str:blog_id>", deleteBlog, name="deleteBlog"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
