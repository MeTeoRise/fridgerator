from django.urls import path
from .views import ItemListView, AddItemView, ShoppingListView, AddShoppingListView, AlertListView, AddAlertView, \
    MaintenanceListView, AddMaintenanceView, SettingsListView, AddSettingsView, EditSettingsView, barcode_upload_view, \
    ItemDeleteView, ShoppingListDeleteView, AlertDeleteView, MaintenanceDeleteView


urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/add/', AddItemView.as_view(), name='add-item'),
    path('items/delete/<int:pk>/', ItemDeleteView.as_view(), name='delete-item'),
    path('shopping-list/', ShoppingListView.as_view(), name='shopping-list'),
    path('shopping-list/add/', AddShoppingListView.as_view(), name='add-shopping-list'),
    path('alerts/', AlertListView.as_view(), name='alerts-list'),
    path('alerts/add/', AddAlertView.as_view(), name='add-alert-list'),
    path('alerts/delete/<int:pk>/', AlertDeleteView.as_view(), name='delete-alert'),
    path('maintenance/', MaintenanceListView.as_view(), name='maintenance-list'),
    path('maintenance/add/', AddMaintenanceView.as_view(), name='add-maintenance-list'),
    path('maintenance/delete/<int:pk>/', MaintenanceDeleteView.as_view(), name='delete-maintenance'),
    path('settings/', SettingsListView.as_view(), name='settings'),
    path('settings/add/', AddSettingsView.as_view(), name='settings-add'),
    path('settings/edit/<int:pk>/', EditSettingsView.as_view(), name='edit-settings'),
    path('items/upload-barcode/', barcode_upload_view, name='upload-barcode'),
    path('shopping-list/delete/<int:pk>/', ShoppingListDeleteView.as_view(), name='delete-shopping-item'),
]
