from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tnsclasses.models import TNS_Class


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        product = get_object_or_404(TNS_Class, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        cart_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
