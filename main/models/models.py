
import asyncio

try:
    from asyncio.windows_events import NULL
except ImportError:
    # Handle non-Windows platform or provide an alternative solution
    pass

from django.db import models
from PIL import Image
from django.db.models import F

class BaseData(models.Model):
    logo_img = models.ImageField(default='chipped2.png', upload_to='company_Logo',null=True, blank=True)
    logo_name = models.CharField(default='Chipped', max_length=100, null=False)
    footer = models.CharField(default='Update Footer ', max_length=100, null=False)
    #impliment the  Singleton pattern
    def save(self, *args, **kwargs):
        if BaseData.objects.count() >= 1:
            existing_data = BaseData.objects.first()
            existing_data.logo_name = self.logo_name
            existing_data.footer = self.footer
            BaseData.objects.filter(pk=existing_data.pk).update(
                logo_img=self.logo_img, logo_name=self.logo_name,
                footer=self.footer,
            )
        else:
            super(BaseData, self).save(*args, **kwargs)

        img = Image.open(self.logo_img.path)
        if img.height > 40 or img.width > 180:
            output_size = (180, 40)
            img.thumbnail(output_size)
            img.save(self.logo_img.path) 
            

