from django.contrib import admin
from django.urls import path, include
from .docs import docs_urls


api_urls = [
    path('someapp/', include('someapp.urls'), name='someapp'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('', include(docs_urls)) # swagger
]
