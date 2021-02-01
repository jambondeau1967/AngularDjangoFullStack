from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
# register url
# http://127.0.0.1:8000/demo/books/
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]
