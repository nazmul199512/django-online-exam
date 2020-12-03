from django.core.exceptions import PermissionDenied


def user_is_student(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'student':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_instructor(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'instructor':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap