from autoslug import AutoSlugField
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class FlatType(models.Model):
    name = models.CharField(max_length=10)
    slug = AutoSlugField(populate_from='name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Flat Type: ' + self.name


class Flat(models.Model):
    scheme = models.ForeignKey(
        'Scheme', on_delete=models.CASCADE, blank=False, null=False, related_name='flats')
    flat_type = models.ForeignKey(
        FlatType, on_delete=models.CASCADE, blank=False, null=False)
    carpet_area = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    accomodation = models.IntegerField(validators=[MinValueValidator(0)])
    estimate_cost = models.BigIntegerField(validators=[MinValueValidator(0)])
    application_amount = models.BigIntegerField(
        validators=[MinValueValidator(0)])
    maintenance_deposit = models.BigIntegerField(
        validators=[MinValueValidator(0)])
    no_of_flats = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Scheme(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    details = models.TextField()
    location = models.TextField(null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    draw_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Scheme Name: ' + self.name
