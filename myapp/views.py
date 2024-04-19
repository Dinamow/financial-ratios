from django.http import JsonResponse
from .models import Engine

ENGINE = Engine()

# Create your views here.
def testing(request):
    if request.method != 'GET':
        return JsonResponse(
            {'error': 'GET request required'},
            status=400)

    years = request.GET.get('years').split(',')
    ratio = request.GET.get('ratio')
    type = request.GET.get('type')
    company = request.GET.get('company')

    if ratio:
        data = {
            "ratio": "current ratio",
                "formula": "current assets / current liabilities",
                "componotes": ["current assets", "current liabilities"],
                "2023": {
                    "value": 1.5,
                    "current assets": 1.5,
                    "current liabilities": 1.0,
                    "numbers": "1.5 / 1.0"
                    },
                "2024": {
                    "value": 1.5,
                    "current assets": 1.5,
                    "current liabilities": 1.0,
                    "numbers": "1.5 / 1.0"
                    }
                }
        return JsonResponse(data,
                            status=200)

    if type:
        data = {
            "ratios": ["current ratio", "quick ratio"],
            "2023": {
                "current ratio": 1.5,
                "quick ratio": 1.5
                },
            "2024": {
                "current ratio": 1.5,
                "quick ratio": 1.5
                }
            }
        return JsonResponse(data,
                            status=200)

    return JsonResponse(
        {'error': 'Invalid request', 'message': 'Please provide type, company, years'},
        status=400)

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
    company = request.GET.get('company')

    if ratio:
        return JsonResponse(ENGINE.get_ratio(ratio, years, company),
                            status=200)

    if type:
        return JsonResponse(ENGINE.get_type(type, years, company),
                            status=200)

    return JsonResponse(
        {'error': 'Invalid request', 'message': 'Please provide type, company, years'},
        status=400)
