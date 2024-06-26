"""the views module"""
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import Engine
import re

ENGINE = Engine()

# Create your views here.
def testing(request):
    """check if the app is running"""
    return JsonResponse({'foo': 'bar'}, status=200)

def landing(request):
    """the landing page view"""
    if request.method != 'GET':
        return JsonResponse(
            {'error': 'GET request required'},
            status=400)
    return render(request, 'index.html')

def view_ratios(request):
    """view ratios page view"""
    if request.method != 'GET':
        return HttpResponseBadRequest('GET request required')
    year = [request.GET.get('year')]
    type = request.GET.get('type')
    company = request.GET.get('company')
    
    if not year or not type or not company:
        return render(request, 'view_ratios.html',
                    context={"dates": ENGINE.get_dates()})

    resp = ENGINE.get_type(type, year, company)

    if 'error' in resp.keys():
        return HttpResponseBadRequest(resp['error'])
    return render(request, 'view_ratios.html',
                  context=resp)

def compare_ratios(request):
    """compare ratios page view"""
    if request.method != 'GET':
        return HttpResponseBadRequest('GET request required')
    
    years = [request.GET.get('year1'),
             request.GET.get('year2')]
    type = request.GET.get('type')
    company: str = request.GET.get('company')

    if not years or not type or not company:
        return render(request, 'compare_ratios.html',
                      context={"dates": ENGINE.get_dates(),
                               'result': {}})
    
    resp = ENGINE.get_type(type, years, company)

    if 'error' in resp.keys():
        return HttpResponseBadRequest(resp['error'])
    return render(request, 'compare_ratios.html',
                  context=resp)


def add_company(request):
    """add company page view"""
    if request.method != 'GET':
        return JsonResponse(
            {'error': 'GET request required'},
            status=400)
    return render(request, 'add_company.html',
                  context={'dates': ENGINE.get_raw()})

        

def save(request):
    """save api to store the ratios data in the db"""
    if request.method != 'POST':
        return JsonResponse(
            {'error': 'POST request required'},
            status=400)

    data = request.POST

    company = data.get('company')
    year = data.get('year')

    if not company:
        return JsonResponse(
            {'error': 'Missing company'},
            status=400)
    
    if not year:
        return JsonResponse(
            {'error': 'Missing year'},
            status=400)

    if ',' in year:
        return JsonResponse(
            {'error': 'Invalid year'},
            status=400)
    
    if not re.match(r'^\d{4}$', year):
        return JsonResponse(
            {'error': 'Invalid year format'},
            status=400)
    
    resp = ENGINE.save_ratios(data)
    if 'error' in resp.keys():
        return JsonResponse(resp, status=400)
    return render(request,
                  'add_company.html',
                  context={'dates': ENGINE.get_raw(),
                           'added': 'true'})

def dates(request):
    """dates api"""
    if request.method != 'GET':
        return JsonResponse(
            {'error': 'GET request required'},
            status=400)
    return JsonResponse(
        {'dates': ENGINE.get_dates()},
        status=200)

def balance(request):
    """balance api"""
    if request.method != 'GET':
        return JsonResponse(
            {'error': 'GET request required'},
            status=400)

    years = request.GET.get('years')
    ratio = request.GET.get('ratio')
    type = request.GET.get('type')
    company: str = request.GET.get('company')

    if not years or years == "":
        return JsonResponse(
            {'error': 'Missing years'},
            status=400)

    if not company:
        return JsonResponse(
            {'error': 'Missing company'},
            status=400)

    company = company.replace('_', ' ')
    years = years.split(',')

    if ratio:
        return JsonResponse(ENGINE.get_ratio(ratio, years, company),
                            status=200)

    elif type:
        resp = ENGINE.get_type(type, years, company)
        if 'error' in resp.keys():
            return JsonResponse(resp, status=400)
        return JsonResponse(resp, status=200)

    elif not type and not ratio:
        resp = ENGINE.get_raw_data(years, company)
        if 'error' in resp.keys():
            return JsonResponse(resp, status=400)
        return JsonResponse(resp, status=200)

    return JsonResponse(
        {'error': 'Invalid request',
         'message': 'Please provide type, company, years'},
        status=400)

def create(request):
    """create api"""
    if request.method != 'GET':
        return HttpResponseBadRequest(
            'GET request required')
    return render(request, 'create.html', context=ENGINE.get_raw())
