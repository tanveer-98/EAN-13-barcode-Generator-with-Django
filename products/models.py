from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
#USE barcode.PROVIDED_BARCODES for all the different barcode types
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    barcode = models.ImageField(upload_to = 'images/',blank = True)
    #we set blank = true because we will generate the barcode so initially it's blank
    countryid = models.CharField(max_length=1,null=True)
    manufacturercode= models.CharField(max_length=6,null=True)
    productcode = models.CharField(max_length = 5,null=True)
    #checkdigit is calcualted automatically
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.countryid}{self.manufacturercode}{self.productcode}',writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.name}.png',File(buffer),save=False)
        return super().save(*args,**kwargs)
