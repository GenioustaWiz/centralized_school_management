from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from schools.models.education_m import EducationStage, EducationLevel
from schools.admin_forms.forms import EducationStageForm, EducationLevelForm

# ================= Education Stage ================= #

class EducationStageListView(ListView):
    model = EducationStage
    context_object_name = 'object_list'
    template_name = 'maindashboard/school/universal/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Education Stage'
        context['model_url'] = 'education_stage'
        context['model_name_plural'] = 'Education Stages'
        return context

class EducationStageDetailView(DetailView):
    model = EducationStage
    context_object_name = 'object'
    template_name = 'maindashboard/school/universal/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_url'] = 'education_stage'
        return context

class EducationStageCreateView(CreateView):
    model = EducationStage
    form_class = EducationStageForm
    template_name = 'maindashboard/school/universal/form.html'
    success_url = reverse_lazy('education_stage_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create Education Stage'
        context['model_url'] = 'education_stage'
        return context

class EducationStageUpdateView(UpdateView):
    model = EducationStage
    form_class = EducationStageForm
    template_name = 'maindashboard/school/universal/form.html'
    success_url = reverse_lazy('education_stage_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Education Stage'
        context['model_url'] = 'education_stage'
        return context

class EducationStageDeleteView(DeleteView):
    model = EducationStage
    template_name = 'maindashboard/school/universal/confirm_delete.html'
    success_url = reverse_lazy('education_stage_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_url'] = 'education_stage'
        return context

# ================ Education Level ==========================#
class EducationLevelListView(ListView):
    model = EducationLevel
    context_object_name = 'object_list'
    template_name = 'maindashboard/school/universal/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Education Level'
        context['model_url'] = 'education_level'
        context['model_name_plural'] = 'Education Levels'
        return context

class EducationLevelDetailView(DetailView):
    model = EducationLevel
    context_object_name = 'object'
    template_name = 'maindashboard/school/universal/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_url'] = 'education_level'
        return context
class EducationLevelCreateView(CreateView):
    model = EducationLevel
    form_class = EducationLevelForm
    template_name = 'maindashboard/school/universal/form.html'
    success_url = reverse_lazy('education_level_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create Education Level'
        context['model_url'] = 'education_level'
        return context

class EducationLevelUpdateView(UpdateView):
    model = EducationLevel
    form_class = EducationLevelForm
    template_name = 'maindashboard/school/universal/form.html'
    success_url = reverse_lazy('education_level_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Education Level'
        context['model_url'] = 'education_level'
        return context

class EducationLevelDeleteView(DeleteView):
    model = EducationLevel
    template_name = 'maindashboard/school/universal/confirm_delete.html'
    success_url = reverse_lazy('education_level_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_url'] = 'education_level'
        return context

