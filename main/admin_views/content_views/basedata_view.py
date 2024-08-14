from django.shortcuts import render
from ...models.models import BaseData

def base_data_view(request):
    try:
        base_data = BaseData.objects.first()
        
    except BaseData.DoesNotExist:
        base_data = None
  
    context ={
        'base_data': base_data,
        }
    return render(request, 
        'maindashboard/base_data/base_data_detail.html',
        context
    )