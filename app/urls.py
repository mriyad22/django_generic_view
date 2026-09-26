from django.urls import path
from .views import *


urlpatterns = [
    path("", StdListView.as_view(), name="list"),
    path("create/", StdCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", StdDetailView.as_view(), name="detail"),
    path("edit/<int:pk>/", StdUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", StdDeleteView.as_view(), name="delete")
]
