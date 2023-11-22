from django.urls import path, reverse_lazy
from A1_perfiles.views import (
    signup_view,
    login_view,
    edit_view,
    logout_view,
    profile_view,
    profile_delete_view,
)

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view.as_view(next_page=reverse_lazy("home")), name="logout"),
    path("perfil/", profile_view, name="perfil"),
    path("edit-profile/", edit_view.as_view(), name="edit"),
    path("delete-profile/", profile_delete_view, name="delete"),
]
