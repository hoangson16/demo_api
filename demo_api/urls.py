from django.contrib import admin
from django.urls import path, include

from core.views import TestView, TestView2

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('test1/', TestView.as_view()),
    path('test2/', TestView2.as_view()),
]
