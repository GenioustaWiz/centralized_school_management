
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.models import EmailAddress

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_auto_signup_allowed(self, request, sociallogin):
        # Override this method to prevent automatic signup
        return False

    def save_user(self, request, sociallogin, form=None):
        # Override this method to delete the associated User model
        user = super().save_user(request, sociallogin, form=form)
        
        # Check if the user has an email address associated
        email = sociallogin.account.extra_data.get('email')
        if email:
            email_address, created = EmailAddress.objects.get_or_create(
                email=email,
                verified=True
            )
            if not created:
                # If the email already exists, update the user reference
                email_address.user = user
                email_address.save()

        # Delete the associated User model
        user.delete()

        return user
