from django.db import models
from django.conf import settings
from src.product.models import Products
from django.utils.translation import gettext_lazy as _


class Orders(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="user_id",
        on_delete=models.CASCADE,
        to_field="username"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderLines(models.Model):
    order = models.ForeignKey(Orders, to_field="user", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, to_field="title", on_delete=models.CASCADE)
    price = models.FloatField(_("product price (GH)"), default=0.0)
    quantity = models.IntegerField(_("quantity"), default=0)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = "Order Lines"
        verbose_name_plural = "Order Lines"
        unique_together = ("order", "product")
