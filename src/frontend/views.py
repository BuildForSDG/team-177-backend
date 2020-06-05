from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def contactus(request):
    return render(request, 'frontend/contactus.html')

def rights(request):
    return render(request, 'frontend/rights.html')

def report(request):
    return render(request, 'frontend/report.html')

def account(request):
    return render(request, 'frontend/account.html')

def legal(request):
    return render(request, 'frontend/legal.html')

def legislative(request):
    return render(request, 'frontend/legislative.html')

def ngao(request):
    return render(request, 'frontend/ngao.html')

def financial(request):
    return render(request, 'frontend/financial.html')

def password(request):
    return render(request, 'frontend/password.html')

def ideology(request):
    return render(request, 'frontend/ideology.html')
