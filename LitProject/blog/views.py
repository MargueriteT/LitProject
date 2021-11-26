from abc import ABC

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from .forms import ReviewRegisterForm, TicketRegisterForm
from .models import Review, Ticket
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.contrib import messages

from userfollows.models import UserFollows


@login_required
def home(request):
    """
    This view return tickets and reviews of the user and and those of
    the users he follows. Display from the most recent to the oldest.
    """

    userfollows = UserFollows.objects.filter(user=request.user)

    all_posts = []

    for review in Review.objects.filter(user=request.user):
        all_posts.append(review)
    for ticket in Ticket.objects.filter(user=request.user):
        if ticket == review.ticket:
            pass
        else:
            all_posts.append(ticket)
    for userfollow in userfollows:
        r = Review.objects.filter(user=userfollow.followed_user)
        for review in r:
            all_posts.append(review)
        t = Ticket.objects.filter(user=userfollow.followed_user)
        for ticket in t:
            all_posts.append(ticket)
    all_posts = sorted(all_posts, key=lambda instance: instance.time_created,
                       reverse=True)
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog/blog.html', context)


@login_required
def user_posts(request):
    """
    This view return tickets and reviews of the user. Display from the most
    recent to the oldest.
    """
    user_posts = sorted(list(chain(Review.objects.filter(user=request.user),
                                   Ticket.objects.filter(user=request.user))),
                        key=lambda instance: instance.time_created,
                        reverse=True)

    context = {
        'user_posts': user_posts
    }
    return render(request, 'blog/user_posts.html', context)


class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    This view return the delete confirmation of a ticket. An user can only
    delete is own ticket.
    """

    model = Ticket
    success_url = reverse_lazy('user_posts')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False



class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    This view return the delete confirmation of a review. An user can only
    delete is own review.
    """

    model = Review
    success_url = reverse_lazy('user_posts')


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    This view return a form to allow an user to update a review. An user can
    only update is own review.
    """

    model = Review
    fields = ['rating', 'headline', 'body']
    template_name = "blog/review_update.html"
    success_url = reverse_lazy('user_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    This view return a form to allow an user to update a ticket. An user can
    only update is own ticket.
    """

    model = Ticket
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('user_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


@login_required
def ResponseCreateReview(request, pk):
    """
    This view is for review create in response to an already existing ticket.
    This view recovers data from the review form. If those are valid, a new
    review is created and a success message is addressed to the user. If
    data aren't valid, the user must change the incorrect field.
    """

    ticket = Ticket.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = ReviewRegisterForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            ticket.response = True
            ticket.save()
            messages.success(request, f'La critique a été ajoutée')
            return redirect('blog-home')

    else:
        form = ReviewRegisterForm()

    context = {'form': form, 'ticket': ticket}

    return render(request, 'blog/review_form.html', context)


def ReviewCreateView(request):
    """
    This view is for a ticket and review creation. The user must complete
    the ticket form and the review form.
    This view recovers data from the ticket form and review form. If those are
    valid, a new review is created and a success message is addressed to the
    user along with the corresponding ticket. If data aren't valid, the user
    must change the incorrect field.
    """

    if request.method == 'POST':
        form_ticket = TicketRegisterForm(request.POST, request.FILES)
        form_review = ReviewRegisterForm(request.POST)
        if form_ticket.is_valid() and form_review.is_valid():
            ticket = form_ticket.save(commit=False)
            ticket.user = request.user
            ticket.response = True
            ticket.save()
            review = form_review.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            messages.success(request, f'La critique a été ajoutée')
            return redirect('blog-home')
    else:
        form_ticket = TicketRegisterForm()
        form_review = ReviewRegisterForm()

    context = {'form_ticket': form_ticket, 'form_review': form_review}

    return render(request, 'blog/new_review.html', context)


def TicketCreateView(request):
    """
    This view is for ticket creation.
    This view recovers data from the ticket form. If those are valid, a new
    ticket is created and a success message is addressed to the user. If
    data aren't valid, the user must change the incorrect field.
    """

    if request.method == 'POST':
        form = TicketRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.response = False
            ticket.save()
            messages.success(request, f'La demande de critique a été ajoutée')
            return redirect('blog-home')
    else:
        form = TicketRegisterForm()

    return render(request, 'blog/ticket_form.html', {'form':form})


class ReviewDetailView(DetailView):
    """
    This view allow the user to see the details of a specific review.
    """

    model = Review


class TicketDetailView(DetailView):
    """
    This view allow the user to see the details of a specific ticket.
    """

    model = Ticket