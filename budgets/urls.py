from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("overview/", views.overview, name="overview"),
    path("transaction/<int:trans_id>", views.transaction, name="transaction")
]
