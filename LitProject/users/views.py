from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UpdateProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView
from .models import Profile
from django.urls import reverse_lazy

def register(request):
    if request.user.is_authenticated:
        return redirect('blog-home')
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def profileUpdateView(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except:
        messages.success(request, f'No profile for  {user.username}')
        return redirect('userfollows-home')

    if request.method == "POST":
        update_profile_form = UpdateProfile(data=request.POST, instance=user_profile)

        if update_profile_form.is_valid():
            profile = update_profile_form.save(commit=False)
            profile.user = request.user

            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            profile.save()
            messages.success(request, f'Profile updated for {profile.user.username}')
            return redirect('userfollows-home')

    else:
        update_profile_form = UpdateProfile(instance=user_profile)

    return render(request, 'users/updateprofile.html', {'form': update_profile_form})


