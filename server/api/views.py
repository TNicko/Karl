from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import api.search as search
import api.gpt as gpt

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [        
        {
            'Endpoint': '/search/',
            'method': 'GET',
            'body': None,
            'description': 'Returns search results'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getSearchResults(request):

    searchTerm = request.query_params['q']
    message = gpt.gpt_response(searchTerm)

    data = {
        'searchTerm': searchTerm,
        'message': message
    }

    return Response(data)