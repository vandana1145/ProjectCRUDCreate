# def decorator_fun(function):
#     print('dec function')
#     def wrapper_func(req, *args, **kwargs):
#         print('request : ', req.user)
        
#         print('wraper function called')
#         return function(req, *args, **kwargs)
#     return wrapper_func

from django.shortcuts import redirect

def unauthenticated_user(function):
    def wrapper_func(req, *args, **kwargs):
        if req.user.is_authenticated:
            return redirect('view')
        else:
            return function(req, *args, **kwargs)
    return wrapper_func