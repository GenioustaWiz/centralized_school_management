

from django.urls import path
from schools.admin_views.school_A_views import *
from schools.admin_views.education_A_views import *
from schools.admin_views.dashboard_views import *

urlpatterns = [
    path('school/dashboard/', school_dashboard_home, name='school_dashboard_home'),
    
    path('education/stages/', EducationStageListView.as_view(), name='education_stage_list'),
    path('education/stages/create/', EducationStageCreateView.as_view(), name='education_stage_create'),
    path('education/stages/<slug:slug>/', EducationStageDetailView.as_view(), name='education_stage_detail'),
    path('education/stages/<slug:slug>/update/', EducationStageUpdateView.as_view(), name='education_stage_update'),
    path('education/stages/<slug:slug>/delete/', EducationStageDeleteView.as_view(), name='education_stage_delete'),

    path('education/levels/', EducationLevelListView.as_view(), name='education_level_list'),
    path('education/levels/create/', EducationLevelCreateView.as_view(), name='education_level_create'),
    path('education/levels/<slug:slug>/', EducationLevelDetailView.as_view(), name='education_level_detail'),
    path('education/levels/<slug:slug>/update/', EducationLevelUpdateView.as_view(), name='education_level_update'),
    path('education/levels/<slug:slug>/delete/', EducationLevelDeleteView.as_view(), name='education_level_delete'),

    path('schools/', SchoolListView.as_view(), name='school_list'),
    path('schools/create/', SchoolCreateView.as_view(), name='school_create'),
    path('schools/<slug:slug>/', SchoolDetailView.as_view(), name='school_detail'),
    path('schools/<slug:slug>/update/', SchoolUpdateView.as_view(), name='school_update'),
    path('schools/<slug:slug>/delete/', SchoolDeleteView.as_view(), name='school_delete'),
]


    