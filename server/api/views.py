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
    # Get search query
    searchTerm = request.query_params['q']

    # Get search results from google
    urls = search.get_search_items(searchTerm)

    # Get response from GPT-3
    gpt_prompt = f"Summarize what is mentioned in following link: {urls[0]}"
    message = gpt.gpt_response(gpt_prompt)

    data = {
        'searchTerm': searchTerm,
        'message': message,
        'urls': urls,
    }
    return Response(data)