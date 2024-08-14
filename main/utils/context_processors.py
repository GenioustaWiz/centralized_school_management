from main.models.models import  ContactSidebarCompanyInfo, BaseData
from main.models.information_footer_M import *

def contact_info(request): 

    contact_info = ContactSidebarCompanyInfo.objects.first()

    
    return {'contact_info': contact_info}

def Top_Footer_Heading(request): 

    Top_Footer_Heading = TopFooterHeading.objects.all()

    
    return {'TopFooterHeadings': Top_Footer_Heading}

def Social_Media_Link(request): 

    Social_Media_Link = SocialMediaLink.objects.first()  # Assuming there's only one instance

    
    return {'SocialMediaLink': Social_Media_Link}

def Base_Data(request): 

    Base_Data = BaseData.objects.first()  # Assuming there's only one instance
    
    print(Base_Data) 
    
    return {'BaseData': Base_Data}