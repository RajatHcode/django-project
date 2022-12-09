from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book_app.views import *

router = DefaultRouter()
router.register(r"users", UserAPIViewSet)
router.register(r"books", BookAPIViewSet)

urlpatterns = router.urls
