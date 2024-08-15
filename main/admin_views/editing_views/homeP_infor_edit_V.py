# from django.shortcuts import render, redirect, get_object_or_404

# from ...models.models import HomePage, programming_languages
# from ...forms.homeP_infor_F import HomePageForm, ProgrammingLanguagesForm


# def edit_home_page(request):
#     # Get the existing home page instance or create a new one if it doesn't exist
#     try:
#         home_page = HomePage.objects.first()
#     except HomePage.DoesNotExist:
#         home_page = HomePage() 

#     if request.method == 'POST':
#         form = HomePageForm(request.POST, instance=home_page)
#         if form.is_valid():
#             form.save()
#             return redirect('home_page_view')  # Replace 'home' with the appropriate URL name for your homepage
#     else:
#         form = HomePageForm(instance=home_page)

#     return render(request,
#         'maindashboard/home_page/edit_home_page.html',
#         {'form': form}
#         )
# # pl = programming_languages
# def edit_pl_page(request, pk=None):
#     if pk:
#         pl = get_object_or_404(programming_languages, pk=pk)
#     else:
#         pl =  programming_languages()
#     if request.method == 'POST':
#         form = ProgrammingLanguagesForm(request.POST, request.FILES, instance=pl)
#         if form.is_valid():
#             form.save()
#             return redirect('home_page_view')  # Redirect to the home page or any other appropriate view
            
#     else:
#         form = ProgrammingLanguagesForm(instance=pl)

#     return render(request,
#         'maindashboard/home_page/edit_programming_languages.html',
#         {'form': form}
#     )
