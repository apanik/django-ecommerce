from django.conf import settings
from django.db import models
from django.shortcuts import reverse

from resources import STRINGS

CATEGORY_CHOICE = (
    ('ST', STRINGS.ST),
    ('SW', STRINGS.SW),
    ('OW', STRINGS.OW)
)

LABEL_CHOICE = (
    ('PR', STRINGS.PR),
    ('SC', STRINGS.SC),
    ('DR', STRINGS.DR)
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    extra_description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    label = models.CharField(choices=LABEL_CHOICE, max_length=2)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ItemDetailView', kwargs={
            "slug": self.slug
        })

    def get_add_to_chart_url(self):
        return reverse('add_to_chart', kwargs={
            "slug": self.slug})

    def get_remove_to_chart_url(self):
        return reverse('remove_to_chart', kwargs={
            "slug": self.slug})


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.item.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.user.username
