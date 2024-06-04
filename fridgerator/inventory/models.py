from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    purchase_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='items_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='shopping_list')
    quantity_needed = models.IntegerField()
    priority = models.CharField(max_length=50)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item.name} - {self.quantity_needed}"


class Alert(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='alerts')
    alert_type = models.CharField(max_length=100)
    message = models.TextField()
    date_issued = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alert_type} - {self.item.name}"


class Maintenance(models.Model):
    issue_description = models.TextField()
    reported_on = models.DateField(auto_now_add=True)
    resolved_on = models.DateField(null=True, blank=True)
    service_contact = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Maintenance Issue Reported on {self.reported_on}"


class Setting(models.Model):
    setting_id = models.AutoField(primary_key=True, default=1)
    temperature_setting = models.DecimalField(max_digits=4, decimal_places=2)
    notification_enabled = models.BooleanField(default=True)
    notification_frequency = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Settings {self.setting_id} - Temperature: {self.temperature_setting}"

