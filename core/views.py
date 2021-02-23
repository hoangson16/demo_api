from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def test_view(request):
    data = {
        'name': 'Son',
        'age': 27,
    }
    return JsonResponse(data)

def test_view2(request):
    data = [
        {
            'name': 'Son',
            'age': 27,
        },
        {
            'name': 'Dat',
            'age': 27,
        },
    ]
    return JsonResponse(data, safe=False)