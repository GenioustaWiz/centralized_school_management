
import os
from django.db import models
from accounts.models import User 
from tinymce.models import HTMLField
from PIL import Image
desc = 'Please write the description here'
class AboutPage(models.Model): 
    heading = models.CharField(default='default', max_length=100, null=False)
    body = HTMLField('Content')

    def save(self, *args, **kwargs):
        if AboutPage.objects.count() >= 1:
            existing_about_page = AboutPage.objects.first()
            existing_about_page.heading = self.heading
            existing_about_page.body = self.body
            AboutPage.objects.filter(pk=existing_about_page.pk).update(
                heading=self.heading, body=self.body
            )
        else:
            super(AboutPage, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        # You can add any custom logic here before deletion, if needed
        super(AboutPage, self).delete(*args, **kwargs)
    
class AboutList(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(default='default', max_length=100, null=False)
    image = models.ImageField(upload_to='about_images',blank=False, null=False)
    desc =  models.TextField(default=desc, max_length=600, null=False)
    
    def save(self, *args, **kwargs):
        super(AboutList, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300) 
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    def delete(self, *args, **kwargs):
        # You can add any custom logic here before deletion, if needed
        # For example, you might want to delete the associated image file
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        
        super(AboutList, self).delete(*args, **kwargs)
    def user_full_name(self):
        if self.user:
            return f"{self.user.first_name} {self.user.last_name}"
        return "P&P AUTO"
    def __str__(self):
        return self.title  # This is used for the model's string representation
    # @classmethod
    # def delete_multiple(cls, ids):
    #     # Delete multiple instances by their IDs
    #     instances = cls.objects.filter(pk__in=ids)
    #     for instance in instances:
    #         instance.delete()