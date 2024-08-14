from django.http import JsonResponse
from django.core import serializers
from .models.models import *
from .models.information_footer_M import TopFooterHeading, TopFooterContent, SocialMediaLink
    

def get_common_data(request):
    contact_info = ContactSidebarCompanyInfo.objects.first()
    base_data = BaseData.objects.first()
    top_footer_headings = TopFooterHeading.objects.all()
    social_media_links = SocialMediaLink.objects.first()  # Assuming there's only one instance

    data = {}

    if contact_info:
        data['contact_info'] = {
            'address': contact_info.address,
            'email': contact_info.email,
            'phone_number': str(contact_info.phone_number),  # Convert PhoneNumber to string
            'whatsapp_url': contact_info.whatsapp,
        }

    if base_data:
        data['base_data'] = {
            'logo_img': str(base_data.logo_img.url),  # Convert ImageField to string
            'logo_name': base_data.logo_name,
            'footer': base_data.footer,
        }
        
    if top_footer_headings:
            top_footer_data = []
            for heading in top_footer_headings:
                heading_data = {
                    'heading': heading.heading,
                    'content_items': []
                }
                content_items = heading.content_items.all()
                for content_item in content_items:
                    content_item_data = {
                        'content': content_item.content,
                        'url': content_item.url
                    }
                    heading_data['content_items'].append(content_item_data)
                top_footer_data.append(heading_data)
            data['top_footer_data'] = top_footer_data

    if social_media_links:
        data['social_media_links'] = {
            'facebook': social_media_links.facebook_link,
            'twitter': social_media_links.twitter_link,
            'whatsapp': contact_info.whatsapp,
            'linkedin': social_media_links.linkedIn_link,
        }

    if data:
        # print('date================')
        # print(data)  
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'information not found.'})
