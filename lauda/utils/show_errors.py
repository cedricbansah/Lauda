from django.shortcuts import redirect
from django.urls import reverse


def show_error(request, error_message):
    request.session['error'] = error_message
    return redirect(reverse('404'))