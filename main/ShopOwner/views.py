from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from ..models import Shop, SubscriptionType, Location, FoodItem
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.utils import render_crispy_form
from django.utils import timezone


def generate_subscription_choose():
    subscription_objects = SubscriptionType.objects.all()
    subscription_list = []
    for subscription in subscription_objects:
        subscription_list.append(
            (str(subscription.id), subscription.description + ": " + str(subscription.price) + " SGD"))
    return subscription_list


def generate_location_choose():
    location_objects = Location.objects.all()
    location_list = []
    for location in location_objects:
        location_list.append((str(location.id), location.area + ", " + location.address))
    return location_list


class NewShopForm(forms.Form):
    shop_name = forms.CharField()

    subscription = forms.ChoiceField(
        choices=(generate_subscription_choose()),
        widget=forms.RadioSelect,
        initial='1',
    )

    location = forms.ChoiceField(
        choices=(generate_location_choose()),
        widget=forms.RadioSelect,
        initial='1',
    )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('shop_name', css_class='input-xlarge'),
        # Field('textarea', rows="3", css_class='input-xlarge'),
        'subscription',
        'location',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )


class NewMealForm(forms.Form):
    name = forms.CharField()
    price = forms.FloatField()

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('name', css_class='input-xlarge'),
        'price',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )


def index(request):
    shop_list = Shop.objects.order_by('name')
    return render(request, 'main/index_shopowner.html', {'shop_list': shop_list})


def shop(request, shop_id):
    current_shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'main/shop.html', {'shop': current_shop})


def newmeal(request, shop_id):
    current_shop = get_object_or_404(Shop, pk=shop_id)
    form = NewMealForm(request.POST or None)
    if form.is_valid():
        # Create the new meal
        new_meal = FoodItem(price=request.POST['price'], name=request.POST['name'],
                            shop_id=shop_id)
        new_meal.save()
        # return to the shop page
        return HttpResponseRedirect(reverse('shopowner:shop', args=(shop_id)))

    return render(request, 'main/newmeal.html', {'form': form})


def newshop(request):
    form = NewShopForm(request.POST or None)
    if form.is_valid():
        # Create the new shop
        new_shop = Shop(name=request.POST['shop_name'], location_id=request.POST['location'],
                        subscription_id=request.POST['subscription'],
                        shop_owner_id=1)  # TODO find the good id
        new_shop.save()

        # return to the shop page
        return HttpResponseRedirect(reverse('shopowner:index'))
    return render(request, 'main/newshop.html', {'form': form})
