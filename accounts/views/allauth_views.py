from allauth.account.views import PasswordSetView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# THIS HELPS WITH REDIRECT FUCTIONALITY ADDS IT THE ORIGINAL PASSWORD_SET
# Found in: venv\Lib\site-packages\allauth\account\views.py

class CustomPasswordSetView(PasswordSetView):

    def get_success_url(self):
        if self.request.user.has_usable_password():
            # User has a password, redirect to the profile page
            return reverse_lazy("profile")
        else:
            # User doesn't have a password, redirect to the password set page
            return reverse_lazy("account_set_password")  # You might need to replace "password_set" with the actual URL name for the password set page

password_set = login_required(CustomPasswordSetView.as_view())

# class CustomPasswordSetView(PasswordSetView):

#     def get_success_url(self):
#         return reverse_lazy("profile")

# password_set = login_required(CustomPasswordSetView.as_view()) 
