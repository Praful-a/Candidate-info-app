from django.shortcuts import HttpResponseRedirect
from django.urls import resolve

# def login_register_middleware(get_response):
#     def middleware(request):
#         url_name = resolve(request.path_info).url_name
#         if (url_name == 'login' or url_name == 'register') and request.user.is_authenticated:
#             response = HttpResponseRedirect('/')
#         else:
#             response = get_response(request)
#         return response
#     return middleware

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        url_name = resolve(request.path_info).url_name
        if (url_name == 'login' or url_name == 'register') and request.user.is_authenticated:
            response = HttpResponseRedirect('/')
        else:
            response = self.get_response(request)
        return response
