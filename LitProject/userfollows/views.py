from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UserFollows
from django.contrib.auth.decorators import login_required
from .forms import NameForm
from django.contrib import messages


@login_required
def userfollows(request):
    """
    This view allow an user to visualize the user he's following. He also
    can check which user he is followed by and search an user by is username
    to start following him thanks to the userfollowed form.
    """

    form = NameForm()

    userfollowed = UserFollows.objects.filter(user=request.user)
    followedby = UserFollows.objects.filter(followed_user=request.user)

    context = {
        'form': form,
        'userfollowed': userfollowed,
        'followedby': followedby

    }
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            UserFollowed = User.objects.filter(username=form.data[
                "name"]).first()
            if UserFollowed:
                newUserFollowed = UserFollows(user=request.user,
                                              followed_user=UserFollowed)

                newUserFollowed.save()

                messages.success(request, f'Nouvel abonnement enregistré')
                return redirect('userfollows-home')
            else:
                messages.error(request, f"Cet abonné n'existe pas")
                return redirect('userfollows-home')

    return render(request,
                  'userfollows/userfollows.html', context)


class UserFollowedDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    This view allow the user to confirm he wants to stop to follow an
    other user.
    """

    model = UserFollows
    success_url = reverse_lazy('userfollows-home')

    def test_func(self):
        userfollows = self.get_object()
        if self.request.user == userfollows.user:
            return True
        return False

