from django.urls import path
from .views import *
from .admin_views.editing_views.basedata_edit_V import edit_base_data
from .admin_views.content_views.basedata_view import *
from .admin_views.dashboard_home_V import *
from .admin_views.content_views.homeP_view_V import home_page_view
from .admin_views.editing_views.homeP_infor_edit_V import *
from .admin_views.editing_views.aboutP_V import *
from .admin_views.editing_views.ContactSidebarCompanyInfo_edit_V import *
from .admin_views.editing_views.information_footer_edit_V import *
from .admin_views.content_views.aboutP_view import *
from .admin_views.content_views.ContactSidebarCompanyInfo_view_V import *
from .admin_views.content_views.top_footer_view_V import *
from .ajax_common_data_send_V import *

urlpatterns = [
    path('', main_index, name='main_index'),
    # AJAX COMMON DATA GET AND SEND
    path('get-common-data/', get_common_data, name='get_common_data'),
    # ==========================
]


# ++++++++++++ Ulrs for Main Admin +++++++++++++++++
urlpatterns += [
    path('main-dashboard/', main_dashboard_home, name='main_dashboard_home'),
    # ===============EDIT HOMEPAGE CONTENT===============
    path('home-page-view/', home_page_view, name='home_page_view'),
    path('edit-home-page/', edit_home_page, name='edit_home_page'),
    path('edit-PL-page/', edit_pl_page, name='edit_pl_page'),
    path('edit-PL-page/<int:pk>/edit/', edit_pl_page, name='edit_pl_page'),
    # =============EDIT BASE DATA===========
    path('basedata-view/', base_data_view, name='base_data_view'),
    path('base_data/edit/', edit_base_data, name='edit_base_data'),
    # ==========EDIT ABOUT PAGE CONTENT=========;
    path('about-page-view/', about_page_view, name='about_page_view'), 
    path('about-page-edit/', about_page_edit, name='about_page_edit'),
    path('about-list-edit/<int:pk>/', about_list_edit, name='about_list_edit'),
    path('about-list/', about_list_edit, name='about_list_edit'),
    # ==========EDIT COMPANY CONTACT INFORMATION======================
    path('company-contact/', companycontact_info_view, name='companycontact_info_view'),
    path('edit-company-contact-info/', edit_company_contact_info, name='edit_company_contact_info'),
    # ============= TOP FOOTER INFORMATION EDIT===========
    path('top-footer-view/', top_footer_view, name='top_footer_view'),
    path('create-top-footer-content/<int:pk>/', create_top_footer_content, name='create_top_footer_content'),
    path('create-top-footer-content/', create_top_footer_content, name='create_top_footer_content'),
    path('create-social-media-links/', create_social_media_links, name='create_social_media_links'),
]
