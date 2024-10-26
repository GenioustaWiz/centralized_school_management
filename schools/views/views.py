
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from django.db.models import Avg, Count
from django.contrib.auth.decorators import login_required
from schools.models.models import School
from schools.models.models_2 import SchoolPerformance, SchoolActivity, Award
from students.models import Student
from teachers.models import Teacher
from schools.models.models_3 import StudentAchievement, FacultyHighlight, GalleryAlbum
from schools.models.news_models import NewsPost, Event

def school_home(request, slug):
    school = get_object_or_404(School, slug=slug)
    
    # Get school statistics
    stats = {
        'total_students': Student.objects.filter(school=school).count(),
        'total_teachers': Teacher.objects.filter(school=school).count(),
        'student_teacher_ratio': round(
            Student.objects.filter(school=school).count() /
            Teacher.objects.filter(school=school).count() 
            if Teacher.objects.filter(school=school).count() > 0 else 0,
            2
        )
    }
    
    # Get recent news
    featured_news = NewsPost.objects.filter(school=school, is_featured=True)[:3]
    recent_news = NewsPost.objects.filter(school=school)[:5]
    
    # Get upcoming events
    today = timezone.now()
    upcoming_events = Event.objects.filter(
        school=school,
        end_date__gte=today
    ).order_by('start_date')[:5]
    
    # Get student achievements
    recent_achievements = StudentAchievement.objects.filter(
        student__school=school
    )[:6]
    
    # Get featured faculty
    featured_faculty = FacultyHighlight.objects.filter(
        teacher__school=school,
        featured=True
    )[:3]
    
    # Get recent gallery albums
    recent_albums = GalleryAlbum.objects.filter(school=school)[:4]
    
    # Get performance metrics
    performance = SchoolPerformance.objects.filter(school=school).order_by('-year')[:5]
    
    # Get activities
    activities = SchoolActivity.objects.filter(school=school).order_by('-date')[:6]
    
    # Get awards
    awards = Award.objects.filter(school=school).order_by('-date_received')[:5]
    
    context = {
        'school': school,
        'stats': stats,
        'featured_news': featured_news,
        'recent_news': recent_news,
        'upcoming_events': upcoming_events,
        'recent_achievements': recent_achievements,
        'featured_faculty': featured_faculty,
        'recent_albums': recent_albums,
        'performance': performance,
        'activities': activities,
        'awards': awards,
    }
    
    return render(request, 'schools/school_home.html', context)

def calendar_view(request, slug):
    school = get_object_or_404(School, slug=slug)
    
    # Get events for the next 30 days
    today = timezone.now()
    thirty_days = today + timedelta(days=30)
    
    events = Event.objects.filter(
        school=school,
        start_date__range=[today, thirty_days]
    ).order_by('start_date')
    
    context = {
        'school': school,
        'events': events,
    }
    
    return render(request, 'schools/calendar.html', context)

def gallery_view(request, slug):
    school = get_object_or_404(School, slug=slug)
    albums = GalleryAlbum.objects.filter(school=school)
    
    context = {
        'school': school,
        'albums': albums,
    }
    
    return render(request, 'schools/gallery.html', context)