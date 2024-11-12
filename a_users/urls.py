from django.urls import path
from a_users.views import profile_edit_view, profile_view


urlpatterns = [
    path("", profile_view, name="profile"),
    path("edit/", profile_edit_view, name="profile-edit"),
]
