from django.forms import ModelForm
from .models import Item
from django.utils.translation import gettext_lazy as _

class ItemForm(ModelForm):
    class Meta:
        # the model to associate with the form
        model = Item
        # a list of all the models' fields you want in the form
        fields = ['description', 'completed']
        labels = {
            'description': _('Item Name'),
            'completed': _('Completed')
        }
