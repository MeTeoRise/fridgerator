from django.views.generic.list import ListView
from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = 'items/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        """ Optionally filter your items here, e.g., by category """
        return Item.objects.all().order_by('expiration_date')  # Example of ordering by expiration date
