from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
import random
import string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from allauth.account.models import EmailConfirmation
from django.core.mail import send_mail

from teachers.serializers import TeacherSerializer
from teachers.models import Teacher
from teachers.forms import TeacherForm   
from accounts.models import User
from accounts.admin_forms.add_other_users_F import UsersRegistrationForm

@login_required
def teacher_register_edit(request, pk=None):
    if pk:  # Edit existing teacher
        teacher = get_object_or_404(Teacher, pk=pk)
        user = teacher.user
    else:  # New teacher registration
        teacher = Teacher()
        user = User()

    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST, instance=teacher)
        user_form = UsersRegistrationForm(request.POST, request.FILES, instance=user)  # Using this to handle user fields

        if teacher_form.is_valid() and user_form.is_valid():
            # Save the user and set user_type to 'teacher'
            user = user_form.save(commit=False)
            user.user_type = 'teacher'
            if pk:
                user.save()
                # Link the teacher to the user
                teacher.user = user
                teacher.save()
                messages.success(request, f'{user.first_name} Edit successfully.')
                return redirect('teacher_A_list') 
            else:
                # Generate a random password
                password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                user.set_password(password)
                user.save()
                # Link the teacher to the user
                teacher.user = user
                teacher.save()
                email = user.email
                print(f'===== new user email===: {email}')
                # Send password email to the user
                messages.success(request, f'{user.first_name} Created successfully.')
                send_generated_password_email(request, email, password)
                return redirect('teacher_register_edit') 
 
    else:
        teacher_form = TeacherForm(instance=teacher)
        user_form = UsersRegistrationForm(instance=user)

    context = {
        'form': teacher_form,
        'user_form': user_form,
        'title': (f'Edit Teacher {user.first_name}' if pk else 'Register Teacher'),
    }

    return render(request, 'maindashboard/p_t_a_universal/form.html', context)

def send_generated_password_email(request, email, password):
    current_site = get_current_site(request)
    
    # Subject of the email
    subject = 'Your Account Registration and Password Information'
    
    # Render the email template with user details and the generated password
    message = render_to_string('emails/generated_password_email.html', {
        'domain': current_site.domain,
        'password': password,  # The generated password
        'support_email': 'support@EdubridgeKe.com',  # You can customize this
    })
    
    # Create the email and set the content type to HTML
    email_message = EmailMessage(subject, message, to=[email])
    email_message.content_subtype = 'html'  # Set the content type to HTML
    email_message.send()

    # ======== to log when the email was sent
    # For instance, using a model to track email confirmation could be useful:
    email_confirmation = EmailConfirmation.create(user)
    email_confirmation.sent = timezone.now()
    email_confirmation.save()
@login_required
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    user = teacher.user
    if request.method == 'POST':
        # teacher.delete()
        user.delete()
        return redirect('teacher_A_list')

    context = {
        'context': user,
        'url_first': 'teacher',
        'title': (f'Delete Teacher {user.first_name} Account' ),
    }
    return render(request, 'maindashboard/p_t_a_universal/confirm_delete.html', context)

# ======== API Access ========
@login_required
class TeacherAPIView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(seriaizer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
