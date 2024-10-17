
from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from students.models import Student
from students.forms import StudentForm
from students.serializers.serializers import StudentSerializer

# ========= ADD or EDIT Students =========
def edit_add_student(request, pk=None):
    #check if primary key is available
    if pk:
        student = get_object_or_404(Student, pk=pk)
    else:
        student = Student()

    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student,)
        print(f"Student Form: {student_form}")
        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.save()
            return redirect('edit_add_student')
    else:
        student_form = StudentForm(instance=student,)
    
    context = {
        'form': student_form,
    }
    return render(request, 'school/dashboard/student/student/add_student.html', context)

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method =='POST':
        student.delete()
        return redirect('student_list')

    context = {
        'student': student,
    }
    return render(request, 'school/dashboard/student/student/student_confirm_delete.html', context)
    
# ========== APIView ===========
class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
