from django.urls import path
from .views import ItemListView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list'),
    path('shopping-list/', ItemListView.as_view(), name='shopping-list'),
    path('alerts/', ItemListView.as_view(), name='alerts-list'),
    path('maintenance/', ItemListView.as_view(), name='maintenance-list'),
    path('settings/', ItemListView.as_view(), name='settings'),
]
