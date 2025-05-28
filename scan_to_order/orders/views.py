from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Table, MenuItem, Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
import json

def menu_view(request, table_number):
    table = get_object_or_404(Table, number=table_number)
    menu_items = MenuItem.objects.filter(available=True)
    context = {
        'table': table,
        'menu_items': menu_items,
    }
    return render(request, 'orders/menu.html', context)

@csrf_exempt
def place_order(request, table_number):
    if request.method == 'POST':
        table = get_object_or_404(Table, number=table_number)
        data = json.loads(request.body)
        items = data.get('items', [])
        if not items:
            return JsonResponse({'error': 'No items provided'}, status=400)
        order = Order.objects.create(table=table)
        for item in items:
            menu_item = get_object_or_404(MenuItem, id=item['id'])
            quantity = item.get('quantity', 1)
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
        return JsonResponse({'message': 'Order placed successfully', 'order_id': order.id})
    return JsonResponse({'error': 'Invalid request method'}, status=405)
