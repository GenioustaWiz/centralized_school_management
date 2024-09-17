
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import logging
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator

from students.models import Student
from accounts.models import User
from students.serializers.student_list_s import StudentListSerializer

def student_list(request):
    # check if the user is Authenticated
    if request.user.is_authenticated:
        # check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/student/student/student_list.html'
        else:
            template_name = 'student/student/student_list.html'
        students = Student.objects.all()
        context = {
            'students': students
        }
        return render(request, template_name, context)

#  =================== APIView =======================
logger = logging.getLogger(__name__)

class StudentListPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class StudentListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StudentListPagination

    def get(self, request):
        logger.info(f"User: {request.user}, Auth: {request.user.is_authenticated}")
        logger.info(f"Request headers: {request.headers}")
        
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=403)
        
        students = Student.objects.all()
        
        # Get pagination parameters from the request
        page = request.query_params.get('page', 1)
        page_size = request.query_params.get('page_size', StudentListPagination.page_size)
        
        # Create a paginator instance
        paginator = Paginator(students, page_size)
        
        try:
            # Get the specified page
            students_page = paginator.page(page)
        except Exception as e:
            logger.error(f"Pagination error: {e}")
            return Response({"detail": "Invalid page."}, status=400)
        
        # Serialize the page of students
        serializer = StudentListSerializer(students_page, many=True)
        
        # Prepare the response
        response_data = {
            "count": paginator.count,
            "next": students_page.has_next() and students_page.next_page_number() or None,
            "previous": students_page.has_previous() and students_page.previous_page_number() or None,
            "results": serializer.data
        }
        
        return Response(response_data)

# class StudentListAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         logger.info(f"User: {request.user}, Auth: {request.user.is_authenticated}")
#         logger.info(f"Request headers: {request.headers}")
        
#         if not request.user.is_authenticated:
#             return Response({"detail": "Authentication credentials were not provided."}, status=403)
        
#         students = Student.objects.all()
#         serializer = StudentListSerializer(students, many=True)
#         return Response(serializer.data)

# class StudentListAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentListSerializer(students, many=True)
#         return Response(serializer.data)


# def student_detail(request):
#     # check if the user is Authenticated
#     if request.user.is_authenticated:
#         # check the user's type, for access limitations
#         if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
#             template_name = 'maindashboard/student/student/student_detail.html'
#         else:
#             template_name = 'student/student/student_detail.html'
#         student = Student.objects.all()
#         context = {
#             'student_detail': student,
#         }
#         return render(request, template_name, context)

    