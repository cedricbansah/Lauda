from django.shortcuts import render, redirect


def errors_view(request):
    if 'error' not in request.session:
        return redirect(request.META['HTTP_REFERER'])


    error_context = {'error': request.session['error']}
    return render(request, "404.html", error_context)