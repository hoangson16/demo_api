from django.contrib import admin
from django.urls import path

from core.views import test_view, test_view2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test1/', test_view),
    path('test2/', test_view2),
]
