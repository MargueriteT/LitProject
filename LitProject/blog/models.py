from django.db import models
from django.conf import settings
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator


class Ticket(models.Model):
    """ Define ticket's attributes """

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cover_image_pics/', null=True,
                              blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    response = models.BooleanField(null=False)

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        if self.image:
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        else:
            pass


class Review(models.Model):
    """ Define review's attributes """

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(5)])
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)