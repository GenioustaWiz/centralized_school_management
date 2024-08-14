from django.shortcuts import render, redirect, get_object_or_404
from ...forms.aboutP_F import AboutPageForm, AboutListForm
from ...models.aboutP_M import *
def about_page_edit(request):
    # Get the existing home page instance or create a new one if it doesn't exist
    try:
        about_page = AboutPage.objects.first()
    except AboutPage.DoesNotExist:
        about_page = AboutPage() 
    if request.method == 'POST':
        form = AboutPageForm(request.POST, instance=about_page)
        if form.is_valid():
            form.save()
            return redirect('about_page_view')  # Replace 'about_page' with the actual URL name
    else:
        form = AboutPageForm(instance=about_page)

    return render(request, 
        'maindashboard/about_page/about_page_template.html', 
        {'form': form}
        )

from django.forms import formset_factory
from django.forms import modelformset_factory

def about_list_edit(request, pk=None):
    # If item_id is provided, get the item to edit, otherwise, create a new item
    if pk is not None:
        item = get_object_or_404(AboutList, pk=pk)
        image= item.image # 
        total_form_count = None
    else:
        total_form_count = None
        item = None 
        image= None 
    # Assuming AboutListForm is your form class
    # WE USE *modelformset_factory* SO THAT WE CAN BE ABLE TO USE QUERYSET ON FORMSET
    AboutListFormSet = modelformset_factory(AboutList, form=AboutListForm, extra=1)  # You can adjust 'extra' as needed
    
    if request.method == 'POST':
        print('==============ID================')
        print(pk)
        if pk is not None: #FOR SAVING EDITED DATA ONLY
            formset =  AboutListForm(request.POST, request.FILES, instance=item)
            if formset.is_valid():
                formset.save()
                return redirect('about_page_view')
            else:
                print('Formset has errors:', formset.errors)
        else: #FOR SAVING NEW DATA
            formset = AboutListFormSet(request.POST, request.FILES,queryset=AboutList.objects.filter(pk=pk))
            print('==============formset================')
            print(formset)
            # Set the 'id' field in the form data before validation
            
            if formset.is_valid():
                # items = formset.save(commit=False)
                # print('==============items================')
                # print(items) 
                for item in formset:
                    itemm = item.save(commit=False)
                    # itemm.user = request.user
                    print('==============instance================') 
                    print(item)  # Check if the form has valid data
                    itemm.save()  # Save the item to the database
                # formset.save_m2m()  # Save many-to-many relationships if any
                return redirect('about_page_view')  # Replace 'about_page' with the actual URL name for your about page
            else:
                print('Formset has errors:', formset.errors)
    else:
        if pk is not None: #FOR SAVING EDITED DATA ONLY
            formset =  AboutListForm(instance=item)
            
        else: #FOR SAVING NEW DATA
            # Fetch the queryset based on the provided primary key (pk)
            queryset = AboutList.objects.filter(pk=pk) if pk is not None else AboutList.objects.none()
            formset = AboutListFormSet(queryset=queryset)
        
            total_form_count = formset.total_form_count()  # Calculate the total number of forms
    context = {
        'formset': formset,
        'image': image,
        'edit_mode': pk is not None,  # True if in edit mode, False if in create new mode
        'total_form_count': total_form_count,
    }

    return render(request, 'maindashboard/about_page/about_list_template.html', context)


