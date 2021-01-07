from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("overview/", views.overview, name="overview"),
]

#Transactions URLs
urlpatterns += [
    path("transactions/", views.TransactionListView.as_view(), name="transactions"),
    path("transactions/create/", views.Transaction_Create.as_view(), name="transaction-create"),
    path("transactions/<int:pk>/", views.TransactionDetailView.as_view(), name="transaction-detail"),
    path("transactions/<int:pk>/update/", views.Transaction_Update.as_view(), name="transaction-update"),
    path("transactions/<int:pk>/delete/", views.Transaction_Delete.as_view(), name="transaction-delete"),
]

#Budgets URLs
urlpatterns += [
    path("budgets/", views.BudgetListView.as_view(), name="budgets"),
    path("budgets/create/", views.Budget_Create.as_view(), name="budget-create"),
    path("budgets/<int:pk>/", views.BudgetDetailView.as_view(), name="budget-detail"),
    path("budgets/<int:pk/update/", views.Budget_Update.as_view(), name="budget-update"),
    path("budgets/<int:pk>/delete/", views.Budget_Delete.as_view(), name="budget-delete"),
]

#Template URLs
urlpatterns += [
    path("template/view", views.template, name="template"),
    path("template/edit", views.template_edit, name="template-edit"),
]

#Bills/Utilities URLs
urlpatterns += [
    path("bills/", views.BillsListView.as_view(), name="bills"),
    path("bills/create", views.Bills_Create.as_view(), name="bill-create"),
    path("bills/<int:pk>/", views.BillsDetailView.as_view(), name="bill-detail"),
    path("bills/<int:pk>/update/", views.Bills_Update.as_view(), name="bill-update"),
    path("bills/<int:pk>/delete/", views.Bills_Delete.as_view(), name="bill-delete"),
]
