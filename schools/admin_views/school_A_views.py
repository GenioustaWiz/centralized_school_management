from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from schools.models.models import School, SchoolContactInfo
from schools.admin_forms.forms import SchoolForm, SchoolContactInfoForm

class SchoolListView(ListView):
    model = School
    context_object_name = 'schools'
    template_name = 'school/dashboard/school/school_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_schools, total_types = School.get_total_schools_and_types()
        context['total_schools'] = total_schools
        context['total_school_types'] = total_types
        return context

class SchoolDetailView(DetailView):
    model = School
    context_object_name = 'school'
    template_name = 'school/dashboard/school/school_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school = self.object
        try:
            context['contact_info'] = SchoolContactInfo.objects.get(name=school)
        except SchoolContactInfo.DoesNotExist:
            context['contact_info'] = None
        print(f'contact info: {context}')
        return context

class SchoolCreateView(CreateView):
    model = School
    form_class = SchoolForm
    template_name = 'school/dashboard/school/school_form.html'
    success_url = reverse_lazy('school_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = SchoolContactInfoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        contact_form = SchoolContactInfoForm(request.POST)
        if form.is_valid() and contact_form.is_valid():
            return self.form_valid(form, contact_form)
        else:
            return self.form_invalid(form, contact_form)

    def form_valid(self, form, contact_form):
        with transaction.atomic():
            self.object = form.save()
            contact_info = contact_form.save(commit=False)
            contact_info.name = self.object
            contact_info.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, contact_form):
        return render(self.request, self.template_name, {'form': form, 'contact_form': contact_form})

class SchoolUpdateView(UpdateView):
    model = School
    form_class = SchoolForm
    template_name = 'school/dashboard/school/school_form.html'
    success_url = reverse_lazy('school_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact_info = SchoolContactInfo.objects.filter(name=self.object).first()
        context['contact_form'] = SchoolContactInfoForm(instance=contact_info)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        contact_info = SchoolContactInfo.objects.filter(name=self.object).first()
        contact_form = SchoolContactInfoForm(request.POST, instance=contact_info)
        if form.is_valid() and contact_form.is_valid():
            return self.form_valid(form, contact_form)
        else:
            return self.form_invalid(form, contact_form)

    def form_valid(self, form, contact_form):
        with transaction.atomic():
            self.object = form.save()
            contact_info = contact_form.save(commit=False)
            contact_info.name = self.object
            contact_info.save()
            print(f'contact info: {contact_info}')
        return redirect(self.get_success_url())

    def form_invalid(self, form, contact_form):
        return render(self.request, self.template_name, {'form': form, 'contact_form': contact_form})

class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'school/dashboard/school/school_confirm_delete.html'
    success_url = reverse_lazy('school_list')












# from django.shortcuts import render, redirect, get_object_or_404
# # from django.views import View
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from schools.models.models import School
# from schools.forms import SchoolForm
# from schools.serializers import SchoolSerializer

# def edit_add_school(request, pk=None):
#     #check if primary key is available
#     if pk:
#         school = get_object_or_404(School, pk=pk)
#     else:
#         school = School()

#     if request.method == 'POST':
#         school_form = SchoolForm(request.POST, instance=school,)
#         print(f"School Form: {school_form}")
#         if school_form.is_valid():
#             school = school_form.save(commit=False)
#             school.save()

#             return redirect('school_list')
#     else:
#         school_form = SchoolForm(instance=school,)
    
#     context={
#         'form': school_form,
#     }
#     return render(request, 'school/dashboard/school/add_school.html', context)

# def school_delete(request, pk):
#     school = get_object_or_404(School, pk=pk)
#     if request.method == 'POST':
#         school.delete()
#         return redirect('school_list')
#     context = {
#         'school': school,
#     }
#     return render(request, 'school/dashboard/school/school_confirm_delete.html', context)
    
# #======= API Access ==========
# class SchoolAPIView(APIView):
#     def get(self, request):
#         schools = School.objects.all()
#         serializer = SchoolSerializer(schools, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = SchoolSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




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
