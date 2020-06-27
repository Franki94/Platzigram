from django.http import HttpResponse, JsonResponse
from datetime import datetime
import json
"""Platzigram views"""

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh hi! Current server time is {now}')

def sort_integers(request):
    """Return a JSON response with sorted integers"""
    numbers = request.GET['numbers'] 
    numbers_list = [int(i) for i in str(numbers).split(',')]
    data = {
        'status':'ok',
        'numbers' : sorted(numbers_list) ,
        'message' : 'Integers sorted successfully'
        }
    # return  JsonResponse(data) #other option
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = f"Sorry {name}, you're not allowed here."
    else:
        message = f"Hello {name}, Welcome to Platzigram"
    return HttpResponse(message)