from django.shortcuts import render


def ind(request):
    return render(request,"main/ind.html")


def about(request):
    return render(request,"main/about.html")

def eshe(request):
    return render(request,"main/eshe.html")

