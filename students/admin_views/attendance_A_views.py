
from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from students.models import Attendance, Student
from students.forms import AttendanceForm
from students.serializers.serializers import  AttendanceSerializer

# ========= ADD or EDIT Attendance =========
def edit_add_attendance(request, student_id):
    # Fetch the student by their ID
    student = get_object_or_404(Student, pk=student_id)
    
    attendance = Attendance(student=student)  # Set the student for the new Attendance

    if request.method == 'POST':
        attendance_form = AttendanceForm(request.POST, instance=attendance,)
        print(f"attendance Form: {attendance_form}")
        if attendance_form.is_valid():
            attendance = attendance_form.save(commit=False)
            attendance.student = student # the student is associated with the performance
            attendance.save()
            return redirect('student_dashboard', pk=student.id,) # Redirect to a student details
    else:
        attendance_form = AttendanceForm(instance=attendance,)
    
    context = {
        'form': attendance_form,
        'student': student,
    }
    return render(request, 'school/dashboard/student/attendance/add_attendance.html', context)

def attendance_delete(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method =='POST':
        attendance.delete()
        return redirect('attendance_list')

    context = {
        'attendance': attendance,
    }
    return render(request, 'school/dashboard/student/attendance/attendance_confirm_delete.html', context)
    
# ========== APIView ===========
class AttendanceAPIView(APIView):
    def get(self, request):
        attendances = Attendance.objects.all()
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
