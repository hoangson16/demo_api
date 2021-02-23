from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from core.views import TestView, TestView2, BaiVietViews

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('test1/', TestView.as_view()),
    path('test2/', TestView2.as_view()),
    path('baiviet/', BaiVietViews.as_view()),
    path('api/token/', obtain_auth_token),
]
