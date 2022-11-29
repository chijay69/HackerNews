from django import template
from ..models import BaseModel

register = template.Library()

@register.simple_tag
def total_items():
     return BaseModel.objects.count()


@register.inclusion_tag('hack/latest_items.html')
def show_latest_items(count=5):
    latest_items = BaseModel.objects.order_by('-by')[:count]
    return {'latest_items': latest_items}
