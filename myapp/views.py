from django.http import JsonResponse
from .models import Engine

ENGINE = Engine()

# Create your views here.
def testing(request):
    return JsonResponse({'foo': 'bar'}, status=200)

def dates(request):
    if request.method != 'GET':
        return JsonResponse(
            {'error': 'GET request required'},
            status=400)
    return JsonResponse(
        {'dates': ENGINE.get_dates()},
        status=200)

def balance(request):
    if request.method != 'GET':
        return JsonResponse(
            {'error': 'GET request required'},
            status=400)

    years = request.GET.get('years').split(',')
    ratio = request.GET.get('ratio')
    type = request.GET.get('type')
    if ratio:
        return JsonResponse(ENGINE.get_ratio(ratio),
                            status=200)
    if type:
        return JsonResponse(ENGINE.get_type(type, years),
                            status=200)
    return JsonResponse(
        {'error': 'Invalid request'},
        status=400)