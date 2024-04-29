from django.shortcuts import render


def errors_view(request):
    return render(request, "404.html")