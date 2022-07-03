from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = 20
    grand_total = 0
    
    if total > 0:
        grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
