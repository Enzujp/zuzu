from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
# Create your views here.


def index(request):
    responseData = {
        'slackUsername': 'enzu',
        'backend': True,
        'age': 23,
        'bio': 'A backend engineer with intentions of making it to the final stage'

    }

    return JsonResponse(responseData)