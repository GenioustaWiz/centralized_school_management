from django.shortcuts import render, redirect
import re
from ...models.models import ContactSidebarCompanyInfo
from ...forms.ContactSidebarCompanyInfo_F import *

def edit_company_contact_info(request):
    company_info = ContactSidebarCompanyInfo.objects.first()
    if request.method == 'POST':
        form = ContactSidebarCompanyInfoForm(request.POST, instance=company_info)
        form2 = ContactSidebarCompanyInfoForm2(request.POST, instance=company_info)
        form3 = ContactSidebarCompanyInfoForm3(request.POST,)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            # Get the WhatsApp number from form2 and create WhatsApp URL
            whatsapp_number = form3.cleaned_data['whatsapp_number']
            whatsapp_url = f'https://wa.me/{whatsapp_number}'

            # Create an instance of the contact model and populate it with data
            contact = ContactSidebarCompanyInfo(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form2.cleaned_data['phone_number'],
                address=form.cleaned_data['address'],
                whatsapp=whatsapp_url, 
            )
            contact.save()
            return redirect('companycontact_info_view')
    else:
        form = ContactSidebarCompanyInfoForm(instance=company_info)
        form2 = ContactSidebarCompanyInfoForm2(instance=company_info)
        form3 = ContactSidebarCompanyInfoForm3()
    
    context={
        'form': form,
        'form2': form2,
        'form3': form3,
        }
    return render(request, 
        'maindashboard/ContactSidebarCompanyInfo/edit_company_contact_info.html',
        context
    )

