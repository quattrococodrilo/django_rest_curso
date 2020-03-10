from django.db import models

# Create your models here.


class Category(models.Model):
    description = models.CharField(
        verbose_name='descripción',
        max_length=100,
    )
    active = models.BooleanField(
        verbose_name='activo',
        default=True,
    )

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
