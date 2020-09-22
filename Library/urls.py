from django.contrib import admin
from django.urls import path, include
from API import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'book', views.BookViewSet)
router.register(r'user', views.UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Book.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
