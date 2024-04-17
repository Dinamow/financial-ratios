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

    years = request.GET.get('years')
    years = years.split(',')
    if len(years) != 2:
        return 
    ratio = request.GET.get('ratio')

    return JsonResponse(
        {'result': years},
        status=200)