from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    
    def get(self, request):
        data = {
            'name': 'Son',
            'age': 27,
        }
        return Response(data)

class TestView2(APIView):

    def get(self, request):
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
        return Response(data)

# def test_view(request):
#     data = {
#         'name': 'Son',
#         'age': 27,
#     }
#     return JsonResponse(data)

# def test_view2(request):
#     data = [
#         {
#             'name': 'Son',
#             'age': 27,
#         },
#         {
#             'name': 'Dat',
#             'age': 27,
#         },
#     ]
#     return JsonResponse(data, safe=False)
