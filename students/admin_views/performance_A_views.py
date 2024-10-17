
from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from students.models import Performance, Student
from students.forms import PerformanceForm
from students.serializers.serializers import PerformanceSerializer

def edit_add_performance(request, student_id, pk=None):
    # Fetch the student by their ID
    student = get_object_or_404(Student, id=student_id)
    
    # Check if a primary key is provided for editing, else create a new performance record
    if pk:
        performance = get_object_or_404(Performance, pk=pk, student=student)
    else:
        performance = Performance(student=student)  # Set the student for the new performance

    if request.method == 'POST':
        performance_form = PerformanceForm(request.POST, instance=performance)
        print(f"Performance Form: {performance_form}")
        if performance_form.is_valid():
            performance = performance_form.save(commit=False)
            performance.student = student  # the student is associated with the performance
            performance.save()
            return redirect('student_dashboard', pk=student.id,)  # (, student_id=student.id) Redirect to a student details
    else:
        performance_form = PerformanceForm(instance=performance)
    
    context = {
        'form': performance_form,
        'student': student,
    }
    return render(request, 'school/dashboard/student/performance/add_performance.html', context)

def performance_delete(request, pk):
    perfomance = get_object_or_404(Performance, pk=pk)
    if request.method =='POST':
        perfomance.delete()
        return redirect('perfomance_list')

    context = {
        'perfomance': perfomance,
    }
    return render(request, 'school/dashboard/student/perfomance/perfomance_confirm_delete.html', context)
    
# ========== APIView ===========
class PerformanceAPIView(APIView):
    def get(self, request):
        perfomances = Performance.objects.all()
        serializer = PerformanceSerializer(perfomances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerformanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
