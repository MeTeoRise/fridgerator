from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Item, Alert, Maintenance, Setting, ShoppingList
from .forms import ItemForm, ShoppingListForm, AlertForm, MaintenanceForm, SettingForm, BarcodeForm
import requests
from django.shortcuts import render, redirect
from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO
from django.utils import timezone
from dotenv import load_dotenv
import os


load_dotenv()

UPCDATABASE_API_TOKEN = os.getenv('UPCDATABASE_API_TOKEN')
UPCDATABASE_BASE_URL = "https://api.upcdatabase.org/product/"


class ItemListView(ListView):
    model = Item
    template_name = 'items/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all().order_by('expiration_date')


class AddItemView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/add_item.html'
    success_url = reverse_lazy('item-list')

    def form_valid(self, form):
        return super().form_valid(form)


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'items/confirm_delete.html'
    success_url = reverse_lazy('item-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirm delete'
        return context


class ShoppingListView(ListView):
    model = ShoppingList
    template_name = 'shopping-list/shopping_list.html'
    context_object_name = 'items'


class AddShoppingListView(CreateView):
    model = ShoppingList
    form_class = ShoppingListForm
    template_name = 'shopping-list/add_shopping_list.html'
    success_url = reverse_lazy('shopping-list')

    def form_valid(self, form):
        return super().form_valid(form)


class ShoppingListDeleteView(DeleteView):
    model = ShoppingList
    template_name = 'shopping_list/confirm_delete.html'
    success_url = reverse_lazy('shopping-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirm Deletion of Shopping Item'
        return context


class AlertListView(ListView):
    model = Alert
    template_name = 'alerts/alert_list.html'
    context_object_name = 'alerts'


class AddAlertView(CreateView):
    model = Alert
    form_class = AlertForm
    template_name = 'alerts/add_alert.html'
    success_url = reverse_lazy('alerts-list')

    def form_valid(self, form):
        return super().form_valid(form)


class AlertDeleteView(DeleteView):
    model = Alert
    success_url = reverse_lazy('alerts-list')
    template_name = 'alerts/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirm Deletion of Alert'
        return context


class MaintenanceListView(ListView):
    model = Maintenance
    template_name = 'maintenance/item_list.html'
    context_object_name = 'items'


class AddMaintenanceView(CreateView):
    model = Maintenance
    form_class = MaintenanceForm
    template_name = 'maintenance/add_item.html'
    success_url = reverse_lazy('item-list')

    def form_valid(self, form):
        return super().form_valid(form)


class MaintenanceDeleteView(DeleteView):
    model = Maintenance
    success_url = reverse_lazy('maintenance-list')
    template_name = 'maintenance/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirm Deletion of Maintenance Record'
        return context


class SettingsListView(ListView):
    model = Setting
    template_name = 'settings/item_list.html'
    context_object_name = 'items'


class AddSettingsView(CreateView):
    model = Setting
    form_class = SettingForm
    template_name = 'settings/add_item.html'
    success_url = reverse_lazy('settings-list')

    def form_valid(self, form):
        return super().form_valid(form)


class EditSettingsView(UpdateView):
    model = Setting
    form_class = SettingForm
    template_name = 'settings/edit_item.html'
    success_url = reverse_lazy('settings')

    def form_valid(self, form):
        return super().form_valid(form)


def barcode_upload_view(request):
    if request.method == 'POST':
        form = BarcodeForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_file = BytesIO(image.read())
            image = Image.open(image_file)

            barcodes = decode(image)
            if barcodes:
                barcode_data = barcodes[0].data.decode('utf-8')
                product_details = get_product_details(barcode_data)
                if product_details and product_details.get('success'):
                    new_item = Item(
                        name=product_details.get('title', 'Unknown Product'),
                        category=product_details.get('category', 'Uncategorized'),
                        quantity=1,
                        purchase_date=timezone.now().date(),
                    )
                    new_item.save()
                    return redirect(reverse('item-list'))
            return render(request, 'items/barcode_form.html', {'form': form, 'error': 'No valid barcode found.'})
    else:
        form = BarcodeForm()
    return render(request, 'items/barcode_form.html', {'form': form})


def get_product_details(barcode_data):
    headers = {'Authorization': f'Bearer {UPCDATABASE_API_TOKEN}'}
    response = requests.get(f"{UPCDATABASE_BASE_URL}{barcode_data}", headers=headers)
    if response.status_code == 200:
        return response.json()
    return None
