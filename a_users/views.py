from django.shortcuts import redirect, render
from a_users.forms import ProfileForm
from django.contrib.auth.decorators import login_required


def profile_view(request):
    user = request.user
    return render(request, "a_users/profile.html", {"user": user})


@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")

    return render(request, "a_users/profile_edit.html", {"form": form})
