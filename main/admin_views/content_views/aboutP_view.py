from django.shortcuts import render
from ...models.aboutP_M import AboutPage, AboutList

def about_page_view(request):
    about_page = AboutPage.objects.first()
    about_list = AboutList.objects.all()
    context = {
        'about_page': about_page,
        'about_list': about_list,
    }
    return render(request,
        'maindashboard/about_page/aboutP_view.html', 
        context
        ) 
