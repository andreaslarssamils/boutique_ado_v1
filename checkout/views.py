from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from .forms import OrderForm


def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51SqdpRPkgudGf81chPGKInh0SMmQeQa5dShGVzKKsglG3IpKayk16QxZFm1U3kR1VuORXiNPLBzASFtcteuTsQYM00voBe0gjp",
        "client_secret": "sk_test_51SqdpRPkgudGf81c1qT4pX1YJY2",
    }

    return render(request, template, context)
