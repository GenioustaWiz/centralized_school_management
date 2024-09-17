from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import User

USER_TYPE_GROUP_MAPPING = {
    'master_admin': 'Master Admin Group',
    'lead_admin': 'Lead Admin Group',
    'data_admin': 'Data Admin Group',
    'teacher': 'Teacher Group',
    'parent': 'Parent Group',
    'student': 'Student Group',
    'government_official': 'Government Official Group',
}

@receiver(post_save, sender=User)
def assign_group_to_user(sender, instance, created, **kwargs):
    # Check if the instance is created or user_type is in update_fields (if provided)
    update_fields = kwargs.get('update_fields')
    if created or (update_fields is not None and 'user_type' in update_fields):
        if instance.user_type is not None:
            group_name = USER_TYPE_GROUP_MAPPING.get(instance.user_type)
            if group_name:
                group, created = Group.objects.get_or_create(name=group_name)
                instance.groups.set([group])


