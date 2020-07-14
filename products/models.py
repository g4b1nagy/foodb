from utils.models import BaseModel
from django.db import models


class Product(BaseModel):

    # Note that when unique is True, you don’t need to specify db_index,
    # because unique implies the creation of an index.
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return self.name


class Batch(BaseModel):

    # models.CASCADE: Django also deletes the object containing the ForeignKey.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    expires_on = models.DateField()

    def __str__(self):
        return '{} ({})'.format(self.product.name, self.expires_on)

    class Meta:
        verbose_name_plural = 'Batches'
