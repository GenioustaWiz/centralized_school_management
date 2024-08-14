from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from ...models.models import BaseData
from ...forms.basedata_F import BaseDataForm

def edit_base_data(request):
    # Get the existing home page instance or create a new one if it doesn't exist
    try:
        base_data = BaseData.objects.first()
    except BaseData.DoesNotExist:
        base_data = BaseData() 

    if request.method == 'POST':
        form = BaseDataForm(request.POST, instance=base_data)
        if form.is_valid():
            form.save()
            return redirect('base_data_view')  # Replace 'home' with the appropriate URL name for your homepage
    else:
        form = BaseDataForm(instance=base_data)

    return render(request,
        'maindashboard/base_data/edit_base_data.html',
        {'form': form}
        )

# class BaseDataUpdateView(UpdateView):
#     model = BaseData
#     form_class = BaseDataForm
#     template_name = 'maindashboard/base_data/edit_base_data.html'
#     success_url = reverse_lazy('base_data_view') 
