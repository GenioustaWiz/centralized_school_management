from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
# from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from allauth.account.models import EmailConfirmation

from accounts.models import User
from accounts.serializers.login_serializer import UserLoginSerializer

@method_decorator(csrf_protect, name='dispatch')
class CustomLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = User.objects.filter(email=email).first()

            if user:
                # Check if user has a password
                if user.has_usable_password():
                    # Authenticate the user
                    user = authenticate(request, username=user.email, password=password)

                    if user is not None:
                        # If first login, redirect to change password
                        if user.first_login:
                            user.first_login = False
                            user.save()
                            return Response({'detail': 'First login, please change your password'}, status=status.HTTP_200_OK)
                        else:
                            # Normal login process
                            login(request, user)
                            # Send back user_type in the response
                            user_type = user.user_type  # Assuming user has a `user_type` field
                            return Response({
                                'detail': 'Login successful',
                                'user_type': user_type  # Include user_type in response
                            }, status=status.HTTP_200_OK)
                    else:
                        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    # Social account without password, send password reset link
                    send_set_password_email(request, email)
                    return Response({'detail': 'Check your email for a password reset link'}, status=status.HTTP_200_OK)

            return Response({'detail': 'No user found with this email'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_set_password_email(request, email):
    current_site = get_current_site(request)
    user = request.user  # Assuming the user is authenticated here
    email_confirmation = EmailConfirmation.create(user)
    email_confirmation.sent = timezone.now()
    email_confirmation.save()


    subject = 'Set a Password'
    message = render_to_string('password_set.html', {
        'user': request.user,
        'domain': current_site.domain,
        'uid': email_confirmation.key,
        'token': email_confirmation.key,
    })
    to_email = [email]
    email = EmailMessage(subject, message, to=to_email)
    email.send()