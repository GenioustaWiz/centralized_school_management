from django.shortcuts import render
from ...models.models import ContactSidebarCompanyInfo

def companycontact_info_view(request):
    company_info = ContactSidebarCompanyInfo.objects.first()
    context = {
        'company_info': company_info
    }
    return render(request, 
        'maindashboard/ContactSidebarCompanyInfo/view_company_contact_info.html',
        context
    )
