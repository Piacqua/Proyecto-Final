from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    contexto = {}
    http_response = render(
        request=request, context=contexto, template_name="index.html"
    )
    return http_response


def about(request):
    contexto = {}
    http_response = render(
        request=request, context=contexto, template_name="about.html"
    )
    return http_response
