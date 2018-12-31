
from django.http import HttpResponse #For loading pure html without using a template
from django.template import loader
from gl_app.models import GroceryItem

def index(request):
    template = loader.get_template('index.html')
    context = {
        'items': GroceryItem.objects.all()
    }
    return HttpResponse(template.render(context, request))