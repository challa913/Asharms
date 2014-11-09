from django.core.validators import MinValueValidator
from django.db import models
from base import Base
from myuser.models import MyUser

__author__ = 'challa'


class Ashrams(Base, models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.IntegerField(max_length=10)
    below_one = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="People with age below 1",
                                    default=0)
    one_to_five = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="age between 1 and 5",
                                      default=0)
    six_to_ten = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="age between 6 and 10",
                                        default=0)
    eleven_to_fourteen = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="between 11 and 14",
                                    default=0)
    fifteen_to_eighteen = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="age between 15 and 18",
                                      default=0)
    nineteen_to_forty = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="between 19 and 40",
                                        default=0)
    forty_to_sixty = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="between 41 and 60",
                                        default=0)
    above_sixty = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="above 60",
                                    default=0)
    user = models.ForeignKey(MyUser)
    ashram_rating = models.IntegerField(max_length=2)
    ashram_pic = models.ImageField()

    class Meta:
        app_label = 'ashrams'
        verbose_name_plural = 'Ashrams'
