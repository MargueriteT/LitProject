from django import forms
from .models import Ticket, Review


class TicketRegisterForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Enter the title'}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={
        'placeholder': 'Please complete your ticket'}))

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewRegisterForm(forms.ModelForm):
    Choices = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    headline = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Enter your headline'}))
    rating = forms.CharField(widget=forms.RadioSelect(choices=Choices),
                             label="Rating")
    body = forms.CharField(label="", widget=forms.Textarea(attrs={
        'placeholder': 'Please complete your review'}))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']



