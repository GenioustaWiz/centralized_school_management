
from django.db import models

class TopFooterHeading(models.Model):
    heading = models.CharField(default='default', max_length=100, null=False)

    def __str__(self): 
        return self.heading
    def save(self, *args, **kwargs):
        super(TopFooterHeading, self).save(*args, **kwargs)

class TopFooterContent(models.Model): 
    heading = models.ForeignKey(TopFooterHeading, on_delete=models.CASCADE, related_name='content_items')
    content = models.CharField(default='default',max_length=200, null=False)
    url = models.URLField(default='https://..', null=True, blank=True)
    
    def __str__(self):
        return self.content
    def save(self, *args, **kwargs):
        super(TopFooterContent, self).save(*args, **kwargs)

class SocialMediaLink(models.Model):
    facebook_link = models.URLField(default='https://www.facebook.com/', null=True, blank=True)
    whatsapp_link = models.URLField(default='https://web.whatsapp.com', null=True, blank=True)
    linkedIn_link = models.URLField(default='https://www.linkedin.com/', null=True, blank=True)
    twitter_link = models.URLField(default='https://twitter.com', null=True, blank=True)

    def save(self, *args, **kwargs):
        super(SocialMediaLink, self).save(*args, **kwargs)