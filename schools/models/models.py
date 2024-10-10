# schools/models.py
from django.db import models
from django.utils.text import slugify
from django.db.models import Sum, Count
from schools.models.education_m import EducationLevel

class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    school_type = models.CharField(max_length=50)
    education_levels = models.ManyToManyField(EducationLevel, blank=True, related_name='schools')
    established_date = models.DateField()
    about = models.TextField(default="please enter school information")
    capacity = models.IntegerField(default="0")
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


class SchoolContactInfo(models.Model):
    name = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schools')
    phone_number = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    address = models.CharField(max_length=200, null=False)
    whatsapp = models.URLField(default="https://wa.me/enternumber")
    
    # ===== Save only one model, avoid duplicates ============= #
    def save(self, *args, **kwargs):
        if SchoolContactInfo.objects.count() >= 1:
            existing_info = SchoolContactInfo.objects.first()
            existing_info.name = self.name
            existing_info.phone_number = self.phone_number
            existing_info.email = self.email
            existing_info.address = self.address
            existing_info.whatsapp = self.whatsapp
            SchoolContactInfo.objects.filter(pk=existing_info.pk).update(
                name=self.name, phone_number=self.phone_number,
                email=self.email,address=self.address,whatsapp=self.whatsapp,
            )
        else:
            super(SchoolContactInfo, self).save(*args, **kwargs)
            

    def __str__(self):
        return f"Contact Info for {self.name}"
