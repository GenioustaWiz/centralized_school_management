from django import forms
from django.contrib.auth.models import Permission, Group

class GroupForm_List(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Group.permissions.through.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'filtered'}),
        required=False
    )
    class Meta:
        model = Group
        fields = ['name', 'permissions']
        
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['codename']

class GroupPermissionForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'original'}),
        required=False
    )

    class Meta:
        model = Permission
        fields = ['permissions']

# class SelectPermissionForm(forms.ModelForm):
#     permissions = forms.ModelMultipleChoiceField(
#         # queryset=Permission.objects.all(),
#         queryset=None,
#         widget=forms.SelectMultiple(attrs={'class': 'filtered','id': 'id_select_permissions', 'multiple': True}),
#         required=False
#     )

#     class Meta:
#         model = Group
#         fields = ['permissions']
class SelectPermissionForm(forms.Form):
    select_permissions = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'filtered', 'id': 'id_select_permissions', 'multiple': True, 'style': 'width: 100%;'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', None)
        super(SelectPermissionForm, self).__init__(*args, **kwargs)

        if queryset is not None:
            choices = [(perm.id, f'{perm.content_type.app_label} | {perm.content_type.model} | {perm.name}') for perm in queryset]
            self.fields['select_permissions'].choices = choices

# class SelectPermissionForm(forms.Form):
#     permissions = forms.MultipleChoiceField(
#         widget=forms.SelectMultiple(attrs={'class': 'filtered','id': 'id_select_permissions', 'multiple': True}),
        
#         required=False
#     )
    # class Meta:
    #     model = Group
    #     fields = ['permissions']