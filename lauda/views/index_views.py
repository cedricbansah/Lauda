from django.shortcuts import render, redirect
from django.urls import reverse


def index_view(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    return render(request, 'index.html')
