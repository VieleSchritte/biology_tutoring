from django.shortcuts import render


def view_start_page(request):
    return render(request, 'startPage.html', {})
