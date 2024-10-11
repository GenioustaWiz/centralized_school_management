from django.db import models
from django.utils.text import slugify

class EducationStage(models.Model):
    STAGES = [
        ('Early Years Education', 'Early Years Education' ),
        ('Upper Primary Education', 'Upper Primary Education'),
        ('Secondary School Education', 'Secondary School Education'),
    ]
    name = models.CharField(max_length=50, choices=STAGES)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    # get_fields() method that returns a list of (field_name, value) tuples
    # this will help reduce templates duplicates
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

class EducationLevel(models.Model):
    CURRICULUM_CHOICES = [
        ('CBC', 'Competency-Based Curriculum'),
        ('8-4-4', '8-4-4 System'),
        ('SNE', 'Special Needs Education'),
    ]

    name = models.CharField(max_length=100)
    stage = models.ForeignKey(EducationStage, on_delete=models.CASCADE, related_name='levels')
    curriculum = models.CharField(max_length=5, choices=CURRICULUM_CHOICES)
    has_sne = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        unique_together = ['name', 'stage', 'curriculum']
        ordering = ['stage', 'order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.stage.name}-{self.name}-{self.curriculum}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.get_curriculum_display()}"
    
    # get_fields() method that returns a list of (field_name, value) tuples
    # this will help reduce templates duplicates
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
