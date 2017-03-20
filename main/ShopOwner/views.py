from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from ..models import Shop


def index(request):
    shop_list = Shop.objects.order_by('name')
    return render(request, 'main/index.html', {'shop_list': shop_list})


def shop(request, shop_id):
    current_shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'main/shop.html', {'shop': current_shop})
