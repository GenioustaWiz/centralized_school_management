# decorators.py
from django.http import HttpResponseForbidden

def user_type_required(*allowed_types):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_superuser or request.user.user_type in allowed_types:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You are not allowed to access this page.")
        return _wrapped_view
    return decorator
    
# def user_type_required(*allowed_types):
    # def decorator(view_func):
    #     def _wrapped_view(request, *args, **kwargs):
    #         if request.user.user_type not in allowed_types:
    #             return HttpResponseForbidden("You are not allowed to access this page.")
    #         return view_func(request, *args, **kwargs)
    #     return _wrapped_view
    # return decorator
