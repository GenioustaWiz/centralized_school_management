# schools/models.py
from django.db import models
from django.utils.text import slugify
from django.db.models import Sum, Count

class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    school_type = models.CharField(max_length=50)
    education_levels = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(School, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    @classmethod
    def get_total_schools_and_types(cls):
        # Count the total number of schools
        total_schools = cls.objects.count()
        
        # Count the distinct number of school types
        distinct_school_types = cls.objects.aggregate(total_types=Count('school_type', distinct=True))
        
        return total_schools, distinct_school_types['total_types']