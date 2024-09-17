from django.db import models
from django.db.models import Sum, Count

from accounts.models import User
from schools.models import School

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    schools = models.ManyToManyField(School, blank=True)  # Allow association with multiple schools
    # Add other relevant fields

    def __str__(self):
        return str(self.user)

    @classmethod
    def get_total_parents_and_schools(cls):
        # Count the total number of parents
        total_parents = cls.objects.count()
        
        # Aggregate the total number of schools associated with all parents
        total_schools = cls.objects.aggregate(total_schools=Count('schools', distinct=True))
        
        return total_parents, total_schools['total_schools']