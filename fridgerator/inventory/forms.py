from django import forms
from .models import Item, ShoppingList, Alert, Maintenance, Setting


class DateInput(forms.DateInput):
    input_type = 'date'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity', 'purchase_date', 'expiration_date', 'location', 'image']
        widgets = {
            'purchase_date': DateInput(),
            'expiration_date': DateInput()
        }


class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ['item', 'quantity_needed', 'priority', 'purchased']


class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['item', 'alert_type', 'message']


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['issue_description', 'resolved_on', 'service_contact']


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ['temperature_setting', 'notification_enabled', 'notification_frequency']


class BarcodeForm(forms.Form):
    image = forms.ImageField()
