from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Shop, User, Customer, FoodItem


def fooditems(request, shop_id):
    shops = Shop.objects.all()
    current_shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'main/fooditems.html', {'shop': current_shop})


def buy_fooditem(request, fooditem_id):
    if not request.user.is_authenticated:
        print("user not authenticated")
        return redirect('home')
    else:
        fooditem = get_object_or_404(FoodItem, pk=fooditem_id)
        current_user = get_object_or_404(Customer, user_id=request.user.id)

        fooditem.shop.shop_owner.credit += fooditem.price
        fooditem.shop.shop_owner.save()

        current_user.balance -= fooditem.price
        current_user.save()
        return render(request, "main/order_confirmation.html")
