# from django.shortcuts import render
# from ...models.models import HomePage, programming_languages
# def home_page_view(request):
#     try:
#         home_page = HomePage.objects.first()
#         tech= programming_languages.objects.all()
#     except HomePage.DoesNotExist:
#         home_page = None
#         # tech = None
#     context ={
#         'home_page': home_page, 
#         'tech': tech,
         
#         }
#     return render(request, 
#         'maindashboard/home_page/homepage_infor.html',
#         context
#     )
