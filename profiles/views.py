from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    """Display the user's profile."""
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request,
                "Update failed. Please ensure the form is valid.",
            )
    else:
        form = UserProfileForm(instance=user_profile)

    orders = user_profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "on_profile_page": True,
    }
    return render(request, template, context)
