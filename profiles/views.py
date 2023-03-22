from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import UserProfile
from .forms import UserProfileForm

from products.models import Product
from checkout.models import Order
from profiles.models import Wishlist


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    context = {'wishlist_items': wishlist_items}
    return render(request, 'profiles/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = Wishlist(user=request.user, product=product)
    wishlist_item.save()
    messages.success(request, "Product Added to your Wishlist")
    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = get_object_or_404(
        Wishlist, user=request.user, product=product)
    wishlist_item.delete()
    messages.success(request, "Product Deleted from your Wishlist")
    return redirect(reverse('wishlist'))
