from django.urls import include, path

from . import routers

urlpatterns = [
    path('', include(routers.router.urls)),  # provides a few default
    # views that we can use for our CRUD operations.
]