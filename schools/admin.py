from django.contrib import admin
from schools.models.models import School
from schools.models.models_2 import SchoolPerformance, SchoolActivity, Award
from students.models import Student
from teachers.models import Teacher
from schools.models.models_3 import StudentAchievement, FacultyHighlight, GalleryAlbum, GalleryImage
from schools.models.news_models import NewsPost, Event

admin.site.register(NewsPost)
admin.site.register(Event)
admin.site.register(StudentAchievement)
admin.site.register(FacultyHighlight)
admin.site.register(SchoolPerformance)
admin.site.register(SchoolActivity)
admin.site.register(Award)
admin.site.register(GalleryAlbum)
admin.site.register(GalleryImage)