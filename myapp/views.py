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
    ratio = request.GET.get('ratio')
    type = request.GET.get('type')
    company = request.GET.get('company')

    if not years:
        return JsonResponse(
            {'error': 'Missing years'},
            status=400)

    years = years.split(',')

    if ratio:
        return JsonResponse(ENGINE.get_ratio(ratio, years, company),
                            status=200)

    if type:
        resp = ENGINE.get_type(type, years, company)
        if 'error' in resp.keys():
            return JsonResponse(resp, status=400)
        return JsonResponse(resp, status=200)
            

    return JsonResponse(
        {'error': 'Invalid request', 'message': 'Please provide type, company, years'},
        status=400)
