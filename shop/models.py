import pandas as pd
from django.core.exceptions import ValidationError
from django.db import models


#  create model of goods with fields: name, price, description with regex validator, date_added

class Goods(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # create validator for field 'date_added' witch should be more than current date
    def clean(self):
        if self.date_added < pd.Timestamp.now():
            raise ValidationError('Date of creation should be more than current date')


# create regular expression 8 symbols and 2 digits, upper and lower case letters and special characters
REGEX_NAME = r'^[A-Za-z0-9]{8}[A-Za-z0-9]{2}$'










