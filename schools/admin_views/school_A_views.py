
from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from schools.models import School
from schools.forms import SchoolForm
from schools.serializers import SchoolSerializer

def edit_add_school(request, pk=None):
    #check if primary key is available
    if pk:
        school = get_object_or_404(School, pk=pk)
    else:
        school = School()

    if request.method == 'POST':
        school_form = SchoolForm(request.POST, instance=school,)
        print(f"School Form: {school_form}")
        if school_form.is_valid():
            school = school_form.save(commit=False)
            school.save()

            return redirect('school_list')
    else:
        school_form = SchoolForm(instance=school,)
    
    context={
        'form': school_form,
    }
    return render(request, 'maindashboard/school/add_school.html', context)

def school_delete(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'POST':
        school.delete()
        return redirect('school_list')
    context = {
        'school': school,
    }
    return render(request, 'maindashboard/school/school_confirm_delete.html', context)
    
#======= API Access ==========
class SchoolAPIView(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class SchoolFormView(View):
#     def get(self, request):
#         form = SchoolForm()
#         return render(request, 'schools/school_form.html', {'form': form})

#     def post(self, request):
#         form = SchoolForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('school_list')  # Assuming you have a school list view
#         return render(request, 'schools/school_form.html', {'form': form})
