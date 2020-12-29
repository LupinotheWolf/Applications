from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("overview/", views.overview, name="overview"),
    path("transactions/", views.TransactionListView.as_view(), name="transactions"),
    path("transactions/create/", views.Transaction_Create.as_view(), name="transaction-create"),
    path("transactions/<int:pk>/", views.TransactionDetailView.as_view(), name="transaction-detail"),
    path("transactions/<int:pk>/update/", views.Transaction_Update.as_view(), name="transaction-update"),
    path("transactions/<int:pk>/delete/", views.Transaction_Delete.as_view(), name="transaction-delete"),
    path('budgets/', views.BudgetListView.as_view(), name='budgets'),
    path('budgets/create/', views.Budget_Create.as_view(), name='budget-create'),
    path('budgets/<int:pk>/', views.BudgetDetailView.as_view(), name='budget-detail'),
    path('budgets/<int:pk/update/', views.Budget_Update.as_view(), name='budget-update'),
    path('budgets/<int:pk>/delete/', views.Budget_Delete.as_view(), name='budget-delete'),
]
