from django.shortcuts import render


def base_view(request):
    return render(request, 'base/base.html')
