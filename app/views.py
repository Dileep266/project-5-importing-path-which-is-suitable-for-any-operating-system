from django.shortcuts import render

# Create your views here.
def virat(request):
    return render(request,'virat.html')
def rohit(request):
    return render(request,'rohit.html')
def jadeja(request):
    return render(request,'jadeja.html')
def dhoni(request):
    return render(request,'dhoni.html')