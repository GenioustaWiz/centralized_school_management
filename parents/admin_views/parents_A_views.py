from django.shortcuts import render, redirect, get_object_or_404
# from django.views import Views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from parents.models import Parent
from parents.forms import ParentForm
from parents.serializers import ParentSerializer

def edit_add_parent(request, pk=None):
    # check if primary key is available
    if pk:
        parent = get_object_or_404(Parent, pk=pk)
    else:
        parent = Parent()

    if request.method == 'POST':
        parent_form = ParentForm(request.POST, instance=parent,)
        print(f"Parent Form: {parent_form}")
        if parent_form.is_valid:
            parent = parent_form.save(commit=False)
            parent.save()

            return redirect('edit_add_parent')
    else:
        parent_form = ParentForm(instance=parent,)

    context = {
        'form': parent_form,
    }

    return render(request, 'maindashboard/parent/add_parent.html', context)

def parent_delete(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    if request.method == 'POST':
        parent.delete()
        return redirect('parent_list')

    context = {
        'parent': parent,
    }
    return render(request, 'maindashboard/parent/parent_confirm_delete.html', context)

# ======== API Access ========
class ParentAPIView(APIView):
    def get(self, request):
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(seriaizer.data)

    def post(self, request):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
