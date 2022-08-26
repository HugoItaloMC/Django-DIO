from django.shortcuts import render, HttpResponse

# Create your views here.


def soma(request, n1, n2):
    n1 = n1 + n2
    return HttpResponse(f" soma {n1}")


def sub(reques, n1, n2):
    n1 = n1 - n2
    return HttpResponse(f" sub {n1}")


def mult(request, n1, n2):
    n1 = n1 * n2
    return HttpResponse(f"multi {n1}")


def divi(request, n1, n2):
    n1 = n1 / n2
    return HttpResponse(f"Divisao {n1}")
