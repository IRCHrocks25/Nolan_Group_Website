from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def buy(request):
    return render(request, 'buy.html')


def sell(request):
    return render(request, 'sell.html')


def luxury(request):
    return render(request, 'luxury.html')


def new_construction(request):
    return render(request, 'new-construction.html')


def communities(request):
    return render(request, 'communities.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def contact(request):
    return render(request, 'contact.html')


def join(request):
    return render(request, 'join.html')
